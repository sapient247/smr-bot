# Сохраняем очищенный файл клавиатур и списков без конфиденциальных названий компаний


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Заменены названия компаний на обобщенные "Demo"
PROJECTS_COMPANIES = {
    'Demo': ['Компания А', 'Компания B', 'Компания C'],
    'Demo1': ['Организация X', 'Организация Y', 'Организация Z']
}

problem = ['Проблема 1', 'Проблема 2', 'Проблема 3']

def get_all_partners(projects_companies):
    all_partners = []
    for key, partners in projects_companies.items():
        all_partners.extend(partners)
    return sorted(set(all_partners))

all_partners = get_all_partners(PROJECTS_COMPANIES)

def get_all_project(projects_companies):
    return sorted(projects_companies.keys())

project = get_all_project(PROJECTS_COMPANIES)

PAGE_SIZE = 50

def create_catalog_all_partners(page=0):
    catalog = ReplyKeyboardMarkup(resize_keyboard=True)
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE

    for partner in all_partners[start:end]:
        catalog.add(KeyboardButton(text=partner))

    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(KeyboardButton(text=f'Page_{page - 1}'))
    if end < len(all_partners):
        navigation_buttons.append(KeyboardButton(text=f'Page_{page + 1}'))

    if navigation_buttons:
        catalog.row(*navigation_buttons)

    catalog.add(KeyboardButton(text='Отмена'))
    return catalog

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Выбрать объект')
main.add(KeyboardButton('Контакты'), KeyboardButton('Формы документов'))
main.add(KeyboardButton('Инструкции'), KeyboardButton('Видео обучение'))

admin = ReplyKeyboardMarkup(resize_keyboard=True)
admin.add('Выбрать объект')
admin.add(KeyboardButton('Контакты'), KeyboardButton('/ask'))
admin.add(KeyboardButton('Инструкции'), KeyboardButton('Видео обучение'))

instructions = ReplyKeyboardMarkup(resize_keyboard=True)
instructions.add(KeyboardButton('Главное меню'))
instructions.add(KeyboardButton('Допуски'))
instructions.add(KeyboardButton('Путь подрядчика'))
instructions.add(KeyboardButton('Инструкция для Партнеров'))

form_pto = ReplyKeyboardMarkup(resize_keyboard=True)
form_pto.add(KeyboardButton('Главное меню'))
form_pto.add(KeyboardButton('Форма 1'))
form_pto.add(KeyboardButton('Форма 2'))

video_training = ReplyKeyboardMarkup(resize_keyboard=True)
video_training.add(KeyboardButton('Главное меню'))
video_training.add(KeyboardButton('Видеоурок 1'))
video_training.add(KeyboardButton('Видеоурок 2'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')

