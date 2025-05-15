import gspread
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import Bot, Dispatcher, types
import keyboards as kb
import main

# Путь к вашему файлу учетных данных
credentials_file = "google_credentials.json"

# Определение области доступа
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Создание учетных данных
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)

# Авторизация и доступ к Google Sheets
client = gspread.authorize(creds)

# Открытие таблицы по ссылке (ссылка очищена)
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/ВАШ_ID_ТАБЛИЦЫ")
sheet = spreadsheet.worksheet("Чек-лист. Свод")

# Получение всех данных с листа
all_data = sheet.get_all_values()

# Определение названий столбцов
header = all_data[0]
data = all_data[1:]

# Определение индексов столбцов
column_map = {name: index for index, name in enumerate(header)}
column_f = column_map.get('Вид работ')
column_c = column_map.get('Параметр контроля')
column_d = column_map.get('Формулировка критерия')
column_e = column_map.get('Ссылка на нормативную документацию')

# Функция для поиска строк по заданным критериям
def find_rows(work_type, control_param):
    result = []
    for row in data:
        if row[column_f] == work_type and row[column_c] == control_param:
            result.append((row[column_d], row[column_e]))
    return result

# Получаем Dispatcher из основного модуля
dp = main.dp

# ID пользователя (опционально, можно убрать)
# user_id = ВАШ_ID_ПОЛЬЗОВАТЕЛЯ

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
