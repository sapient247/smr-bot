Телеграм-бот для автоматизации взаимодействия с подрядчиками.
Реализован на Python с использованием aiogram, Google Sheets API (через gspread), FSM, apscheduler и других библиотек.

📌 Назначение
Приём заявок через интерактивную FSM-форму.

Рассылка ресурсов: инструкции, шаблоны документов, обучающие видео.

Мониторинг статусов и повторные уведомления о невыполненных задачах.

Хранение данных: все обращения автоматически сохраняются в Google Sheets.

🚀 Быстрый старт
Клонировать репозиторий

bash
Копировать
Редактировать
git clone https://github.com/sapient247/smr-bot.git
cd smr-bot
Создать и активировать виртуальное окружение

bash
Копировать
Редактировать
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
Установить зависимости

bash
Копировать
Редактировать
pip install -r requirements.txt
Настроить файл .env

dotenv
Копировать
Редактировать
BOT_TOKEN=<ваш_токен_бота>
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/<ID_таблицы>
CLICKHOUSE_DSN=<строка_подключения_к_ClickHouse>
Запустить бота

bash
Копировать
Редактировать
python main.py
💻 Запуск в Google Colab
Открыть Google Colab

Загрузить файлы проекта

Установить зависимости:

bash
Копировать
Редактировать
!pip install aiogram gspread oauth2client python-dotenv openpyxl pandas apscheduler clickhouse-connect
Вручную задать переменные окружения (BOT_TOKEN, SPREADSHEET_URL, CLICKHOUSE_DSN)

Запустить main.py

🗂 Структура проекта
bash
Копировать
Редактировать
smr-bot/
├── .env                     # Переменные окружения
├── main.py                  # Точка входа
├── bot.py                   # Инициализация и регистрация хендлеров
├── config/                  # Конфигурация для разных окружений
├── handlers/                # Обработчики команд и FSM-сценариев
├── models/                  # Схемы данных / ORM-модели
├── services/                # Взаимодействие с БД, Google Sheets, ClickHouse
├── utils/                   # Вспомогательные функции и логгер
├── send_daily_reminders.py  # Пакетная задача для напоминаний
├── keyboards.py             # Разметка кнопок и inline-меню
├── requirements.txt         # Зависимости
├── google_credentials.json  # Учётные данные Google API
└── README.md                # Инструкция и описание
✅ Возможности
Команды: /start, /help, /id, /ask

FSM-сценарий для приёма заявок

Проверка рейтингов по ИНН / региону / партнёру

Ответы с документами, видео, кнопками и inline-меню

Уровни доступа: пользователь, админ, разработчик

Автоматические ежедневные напоминания

📦 Основные библиотеки
aiogram

gspread + oauth2client

apscheduler

clickhouse-connect

openpyxl + pandas

python-dotenv

❗ Что не включено в репозиторий
В целях безопасности и соблюдения NDA не публикуются:

Реальные токены и учётные данные

Структура корпоративной БД и таблиц

Внутренняя бизнес-логика, примеры данных, шаблоны документов

👤 Автор
Проект разработан для демонстрации автоматизации взаимодействия с подрядчиками в Telegram.

GitHub: sapient247/smr-bot
