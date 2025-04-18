
# smr-bot
smr-bot/
├── bot/                  # Telegram бот (код)
│   ├── main.py
│   ├── database.py
│   └── ...
├── diagrams/             # Диаграммы из Draw.io
│   ├── as_is.png
│   ├── to_be.png
│   ├── use_case.png
│   ├── er_diagram.png
│   └── ...
├── frontend/             # Прототип (HTML/CSS)
│   └── index.html
├── sql/                  # SQL-скрипты для БД
│   ├── schema.sql
│   └── queries.sql
├── .gitignore
├── README.md
└── LICENSE
Автоматизация сопровождения СМР через Telegram-бота
Telegram Bot for Task Management (SQLite-based)

🔧 Описание

Бот помогает отслеживать задачи, отправлять напоминания и вести учёт вопросов/ответов. Изначально он использовал Google Sheets, но теперь работает на SQLite.

📦 Установка

git clone https://github.com/yourusername/your-bot-repo.git
cd your-bot-repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

⚙️ Настройка

Создайте файл .env по шаблону из .env.example:

DB_PATH=bot_database.db

Убедитесь, что у вас установлен Aiogram и Python 3.10+

🗃 Структура Базы Данных

users — ID, имя, логин, фамилия

items — задачи пользователя

questions — вопросы/ответы

🚀 Запуск

python main.py

или подключите как модуль Telegram-бота через aiogram

⏰ Напоминания

Функция send_daily_reminders отправляет уведомления, если задача активна и не закрыта.

✅ ToDo

Добавить фильтрацию по статусу

Добавить поддержку PostgreSQL / MySQL в будущем

📁 .gitignore (рекомендуемый)

.env
*.db
__pycache__/
*.pyc

🤝 Контрибьютинг

Pull requests welcome!
