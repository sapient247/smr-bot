# database.py

from abc import ABC, abstractmethod
from clickhouse_driver import Client as CHClient
import os

class BaseStorage(ABC):
    @abstractmethod
    def create_request(self, user_id: int, request_type: str, payload: dict) -> int:
        pass

    @abstractmethod
    def get_pending_requests(self) -> list[dict]:
        pass

    # ... другие методы доступа по аналогии с gspread-версией

class SheetsStorage(BaseStorage):
    def __init__(self, sheet_url: str, creds_json: str):
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
        self.sheet = gspread.authorize(creds).open_by_url(sheet_url).sheet1

    def create_request(self, user_id: int, request_type: str, payload: dict) -> int:
        row = [user_id, request_type, payload.get('text', ''), 'new']
        return self.sheet.append_row(row)

    def get_pending_requests(self) -> list[dict]:
        records = self.sheet.get_all_records()
        return [r for r in records if r['status'] == 'new']

    # ...

class ClickHouseStorage(BaseStorage):
    def __init__(self):
        # Клиент ClickHouse внутри корпоративной сети
        self.client = CHClient(
            host=os.getenv('CH_HOST'),
            port=os.getenv('CH_PORT', 9000),
            user=os.getenv('CH_USER'),
            password=os.getenv('CH_PASS'),
            database=os.getenv('CH_DB')
        )

    def create_request(self, user_id: int, request_type: str, payload: dict) -> int:
        # Предполагаем, что есть таблица smr_requests с автоинкрементом id
        self.client.execute(
            'INSERT INTO smr_requests (user_id, type, payload, status, created_at) VALUES',
            [(user_id, request_type, payload, 'new', 'now()')]
        )
        # В ClickHouse нет автоинкремента, нужно возвращать, например, запись последнего batch_id
        return 0  

    def get_pending_requests(self) -> list[dict]:
        rows = self.client.execute(
            "SELECT id, user_id, type, payload FROM smr_requests WHERE status = 'new'"
        )
        return [
            {'id': r[0], 'user_id': r[1], 'type': r[2], 'payload': r[3]}
            for r in rows
        ]

    # ...

# Выбор хранилища по переменной окружения
def get_storage() -> BaseStorage:
    if os.getenv('STORAGE_BACKEND') == 'clickhouse':
        return ClickHouseStorage()
    else:
        return SheetsStorage(
            sheet_url=os.getenv('SHEET_URL'),
            creds_json=os.getenv('GOOGLE_CREDS')
        )
