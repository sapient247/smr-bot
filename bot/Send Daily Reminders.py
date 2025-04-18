# send_daily_reminders.py (адаптировано под SQL)
import sqlite3
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import BotBlocked

DB_PATH = "bot_database.db"

async def send_message_with_keyboard(bot, chat_id, text, keyboard=None):
    try:
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard)
    except BotBlocked:
        print(f"Бот заблокирован пользователем {chat_id}. Сообщение не отправлено.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения пользователю {chat_id}: {e}")

async def send_daily_reminders(bot):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = datetime.today().strftime('%Y-%m-%d')

    try:
        cursor.execute("SELECT rowid, * FROM items")
        rows = cursor.fetchall()

        for row in rows:
            row_id = row[0]
            user_id = row[1]
            user_name = row[2]
            name = row[3]
            desc = row[4]
            comment = row[5]
            item_type = row[6]
            timestamp = row[7]

            await send_message_with_keyboard(
                bot=bot,
                chat_id=user_id,
                text=f"Напоминание о задаче: {name}\nТип: {item_type}\nКомментарий: {comment}\nДата: {timestamp}"
            )

            # здесь можно реализовать обновление статуса напоминания, если необходимо

    except Exception as e:
        print(f"Ошибка при работе с базой: {e}")
    finally:
        conn.close()
