# Telegram Bot Demo

**Телеграм-бот для автоматизации взаимодействия с подрядчиками**

**Demo:** Telegram Bot Demo  
**Tech stack:** Python, [aiogram](https://docs.aiogram.dev/), Google Sheets API, FSM, [gspread](https://github.com/burnash/gspread), APScheduler и другие.

---

## 📌 Назначение

- Приём заявок через FSM-форму  
- Автоматическая рассылка инструкций, шаблонов документов, обучающих видео  
- Мониторинг решений и повторное уведомление пользователей  
- Хранение и аналитика заявок в Google Sheets

---

## 🚀 Быстрый старт

1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/sapient247/smr-bot.git
   cd smr-bot```

**Создать и активировать виртуальное окружение**
   ```python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows```

**Установить зависимости**
      pip install -r requirements.txt```

**Настроить .env**

   BOT_TOKEN=your_telegram_bot_token
   SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/your_spreadsheet_id
   CLICKHOUSE_DSN=clickhouse://user:pass@clickhouse.company.local:9000/db

```python main.py
smr-bot/
├── main.py                   # Точка входа, запуск бота
├── database.py               # ClickHouse / SQLite wrapper
├── send_daily_reminders.py   # Скрипт ежедневных напоминаний (APScheduler)
├── keyboards.py              # Inline и Reply клавиатуры
├── handlers/                 # Папка с модулями-обработчиками команд и FSM
│   ├── start.py
│   ├── ask.py
│   └── ...
├── utils/                    # Вспомогательные функции
│   ├── sheets.py             # Google Sheets client
│   └── notifications.py      # Уведомления
├── requirements.txt          # Зависимости
├── .env                      # Конфиденциальные настройки
├── README.md                 # Этот файл
└── google_credentials.json   # Service Account для gspread```

✅ Возможности бота
📜 Команды: /start, /help, /id, /ask

📝 FSM-обработка заявок от подрядчиков

📊 Запись и аналитика заявок в Google Sheets

🔔 Авто-рассылки: инструкции, шаблоны, напоминания

👥 Уровни доступа: пользователь, админ, разработчик

🎥 Отправка видео и документов через бот-меню

❗ Что не включено
В целях безопасности и соблюдения NDA:

Реальные токены, ID пользователей

Логины Telegram-пользователей

Реальная структура корпоративной СУБД

Примеры внутренних инструкций и шаблонов

👤 Автор
Проект разработан в образовательных целях для демонстрации автоматизации взаимодействия с подрядчиками через Telegram-бот.

GitHub: sapient247/smr-bot
