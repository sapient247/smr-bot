# Подготовка очищенного файла с демонстрационным кодом работы с Google Sheets API
# Удалены ссылки, реальные имена пользователей, путь к credentials и реальные данные таблиц


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import asyncio
from datetime import datetime
import os

# Использование переменных окружения
credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE", "google_credentials.json")
spreadsheet_url = os.getenv("SPREADSHEET_URL")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Авторизация
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.authorize(creds)

# Доступ к Google Sheets (используется переменная окружения)
spreadsheet = client.open_by_url(spreadsheet_url)
sheet = spreadsheet.worksheet("bot")
directory = spreadsheet.worksheet("directory")
sheet_question = spreadsheet.worksheet("questions")

# Инициализация БД
async def db_start():
    print("Database initialized")

# Добавление пользователя при старте
async def cmd_start_db(user_id, first_name, username, last_name):
    records = directory.get_all_records()
    user_exists = any(record.get("ID") == user_id for record in records)

    if not user_exists:
        directory.append_row([user_id, first_name, username, last_name])
        print(f"New user added: {user_id}")
    else:
        print(f"User already exists: {user_id}")

# Добавление заявки
async def add_item(state, user_id, user_name):
    async with state.proxy() as data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([user_id, user_name, data.get('name'), data.get('desc'), data.get('comment'), data.get('type'), timestamp])
        print("Item added")

# Запись вопросов и ответов
async def record_question_and_answer(user_id, username, text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet_question.append_row([user_id, username, text, timestamp])
    print(f"Recorded Q&A for user {user_id}")

# Тестовый запуск
async def main():
    await db_start()
    await cmd_start_db("demo_user", "John", "john_doe", "Doe")
    class DummyState:
        async def proxy(self):
            return {'name': 'Issue', 'desc': 'Some description', 'comment': 'Needs fixing', 'type': 'DemoType'}
    await add_item(DummyState(), "demo_user", "John")
    await record_question_and_answer("demo_user", "john_doe", "Sample question")

if __name__ == "__main__":
    asyncio.run(main())



