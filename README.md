MASIS Telegram Bot (Demo)
Телеграм-бот для автоматизации взаимодействия с подрядчиками. Реализован с использованием aiogram, Google Sheets API, FSM, gspread и других библиотек.
📌 Назначение
Бот предназначен для:
- Приема заявок через FSM-форму
- Рассылки инструкций, шаблонов документов и обучающих видео
- Мониторинга решений и повторного уведомления пользователей
- Хранения информации в таблице Google Sheets
🚀 Быстрый старт
1. Клонировать репозиторий:
   git clone https://github.com/yourusername/masis-demo-bot.git
   cd masis-demo-bot

2. Создать виртуальное окружение и активировать его:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. Установить зависимости:
   pip install -r requirements.txt

4. Настроить файл .env:
   BOT_TOKEN=your_telegram_bot_token
   SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/your_spreadsheet_id

5. Запустить бот:
   python main.py
💻 Запуск в Google Colab
1. Открыть Google Colab
2. Загрузить все файлы проекта
3. Установить зависимости:
   !pip install aiogram gspread oauth2client python-dotenv openpyxl pandas apscheduler
4. Вставить токен вручную
5. Запустить main.py
🗃 Структура проекта
masis-demo-bot/
├── main.py
├── database.py
├── send_daily_reminders.py
├── keyboards.py
├── requirements.txt
├── .env
├── README.md
└── google_credentials.json
✅ Возможности бота
- /start, /help, /id, /ask — команды
- FSM-обработка заявок от пользователей
- Проверка рейтингов по ИНН/региону/партнеру
- Ответы с документами, видео, кнопками и inline-меню
- Уровни доступа: пользователь, админ, разработчик
- Автоматические напоминания пользователям о задачах
📦 Библиотеки
- aiogram
- gspread
- oauth2client
- apscheduler
- openpyxl
- pandas
- python-dotenv
❗ Что не включено в репозиторий
В целях безопасности и соблюдения NDA:
- Реальные токены, ID пользователей
- Логины Telegram-пользователей
- Реальная Google таблица и её структура
- Вся внутренняя логика компании (примеры данных, инструкции, шаблоны документов)
👤 Автор
Проект разработан в образовательных целях для демонстрации автоматизации взаимодействия с подрядчиками через Telegram-бот.

Контакты:
Telegram: @yourusername
GitHub: github.com/yourusername

⚠️ ВНИМАНИЕ: При использовании данного шаблона в рабочих системах убедитесь в защите данных, скрытии токенов и соблюдении политик компании.
