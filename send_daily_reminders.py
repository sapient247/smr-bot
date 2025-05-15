# Очистим код от конфиденциальных ссылок, ключей, названий и подготовим безопасный для публикации файл


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from aiogram.utils.exceptions import BotBlocked
import os

# Используем переменные окружения
credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE", "google_credentials.json")
spreadsheet_url = os.getenv("SPREADSHEET_URL")

# Авторизация
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
client = gspread.authorize(creds)

# Подключение к Google таблицам
spreadsheet = client.open_by_url(spreadsheet_url)
sheet = spreadsheet.worksheet("bot")

# Отправка сообщений с клавиатурой
async def send_message_with_keyboard(bot, chat_id, text, keyboard=None):
    try:
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)
    except BotBlocked:
        print(f"Bot blocked by user {chat_id}.")
    except Exception as e:
        print(f"Error sending message to {chat_id}: {e}")

# Основная логика напоминаний
async def send_daily_reminders(bot):
    try:
        records = sheet.get_all_records()
        today = datetime.today().strftime('%d.%m.%Y')

        for row in records:
            user_id = row.get('ID')
            if not user_id:
                continue

            # Первичное уведомление
            if row.get('Уведомление') != 'Да':
                description = row.get('Проблематика')
                date = row.get('Дата обращения')
                contragent = row.get('Контрагент')
                comment = row.get('Комменатрии')
                login = row.get('Телеграм логин')
                project = row.get('Проект')
                row_id = records.index(row) + 2

                await send_message_with_keyboard(
                    bot, user_id,
                    f"Задача: {description} от {date}. Контрагент: {contragent}. Комментарии: {comment}. Контакт: {login}. Проект: {project}."
                )
                sheet.update_cell(row_id, 15, 'Да')  # Уведомление = Да

            # Повторное напоминание
            try:
                date_resolution = datetime.strptime(row.get('Дата решения'), '%d.%m.%Y')
                today_date = datetime.strptime(today, '%d.%m.%Y')
            except ValueError:
                continue

            if row.get('Решено?') != 'Да' and date_resolution < today_date and row.get('Ответ получен?') != 'Да':
                row_id = records.index(row) + 2
                keyboard = InlineKeyboardMarkup()
                keyboard.add(
                    InlineKeyboardButton("Да", callback_data=f"resolve_{row_id}"),
                    InlineKeyboardButton("Нет", callback_data=f"no_{row_id}")
                )
                await send_message_with_keyboard(
                    bot, user_id,
                    f"Напоминание о проблеме: {row.get('Проблематика')} от {row.get('Дата обращения')}.\n"
                    f"Контрагент: {row.get('Контрагент')}, Комментарии: {row.get('Комменатрии')}, "
                    f"Проект: {row.get('Проект')}. Контакт: {row.get('Телеграм логин')}. Решено?",
                    keyboard
                )

            # Подтверждение со стороны контрагента
            if row.get('Контрагент подтверждает решение?') not in ['Да', 'Нет'] and row.get('Решено?') == 'Да':
                initiator_id = row.get('ID инициатора')
                if initiator_id:
                    row_id = records.index(row) + 2
                    keyboard = InlineKeyboardMarkup()
                    keyboard.add(
                        InlineKeyboardButton("Да", callback_data=f"resolve2_{row_id}"),
                        InlineKeyboardButton("Нет", callback_data=f"no2_{row_id}")
                    )
                    await send_message_with_keyboard(
                        bot, initiator_id,
                        f"Подтверждаете решение проблемы: {row.get('Проблематика')} от {row.get('Дата обращения')}?\n"
                        f"Контрагент: {row.get('Контрагент')}, Комментарии: {row.get('Комменатрии')}, "
                        f"Проект: {row.get('Проект')}.",
                        keyboard
                    )

    except gspread.exceptions.GSpreadException as e:
        print(f"Google Sheets API error: {e}")

