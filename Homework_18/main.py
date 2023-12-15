import json
import requests
import datetime as dt


# Задача 1
# https://api.nasa.gov/ - документация 
# Напишите запрос на получение данных за ваши последние выходные. В запросе должны быть данные за три дня (даже если выходной в один день, возьмите 2 дня до, или после, или и до и после)


date = dt.datetime(2023,12,10)

start_date = date - dt.timedelta(days=2)
start_date = start_date.strftime('%Y-%m-%d')
end_date = date.strftime('%Y-%m-%d')

KEY = 'api_key=AAoTekt7FdEXMjh3KmxhXHDh8UMtg5JCMCEoNfLb'
url = f'https://api.nasa.gov/planetary/apod?{KEY}&start_date={start_date}&end_date={end_date}'
file_name = 'task_1.json'

def get_last_weekend(url, file_name):
    response = requests.get(url)
    if response.status_code == 200: 
        with open(file_name, 'w') as file: 
            json.dump(response.json(), file, indent=4)
    else:
        print('Мне не удалось получить запрашиваемую информацию.')

get_last_weekend(url, file_name)



# Задача 2
# https://api.nasa.gov/ - документация 
# напишите запрос на получение данных за день пасхи любого года в пределах 1995 до 2023

easter = dt.datetime(2020,4,19).strftime('%Y-%m-%d') # Взял дату пасхи за 2020 год. 19 апреля 2020 г.

KEY = 'api_key=AAoTekt7FdEXMjh3KmxhXHDh8UMtg5JCMCEoNfLb'
url = f'https://api.nasa.gov/planetary/apod?{KEY}&date={easter}'

file_name = 'task_2.json'

def get_easter(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'w') as file:
            json.dump(response.json(), file, indent=4)
    else:
        print('Мне не удалось получить запрашиваемую информацию.')

get_easter(url, file_name)



# Задача 3
# Создайте приложение для управления пользовательскими настройками. Реализуйте функции для изменения темы приложения, языка интерфейса и настроек уведомлений.
# Хранение пользовательских настроек:
# Формат данных в JSON:
# {
#     "user_settings": {
#         "theme": "dark",
#         "language": "en",
#         "notifications": true
#     }
# }


def user_settings(theme, language, notifications):
    user_settings = {
        'theme': theme,
        'language': language,
        'notifications': notifications
    }
    return user_settings


def choice_theme():
    choice = None
    while choice != '1' and choice != '2':
        print('''
Вам доступны темы:
    1. Светлая
    2. Темная''')
        choice = input('Ваш выбор: ')

    match choice:
        case '1':
            return 'light'
        case '2':
            return 'dark'


def choice_language():
    choice = None
    while choice != '1' and choice != '2':
        print('''
Вам доступны следующие языки:
    1. Русский
    2. Английский''')
        choice = input('Ваш выбор: ')

    match choice:
        case '1':
            return 'ru'
        case '2':
            return 'en'


def choice_notifications():
    choice = None
    while choice != '1' and choice != '2':
        print('''
Желаете ли вы получать уведомления:
    1. Да
    2. Нет''')
        choice = input('Ваш выбор: ')

    match choice:
        case '1':
            return True
        case '2':
            return False
        

def main(file_name):
    theme = choice_theme()
    language = choice_language()
    notifications = choice_notifications()
    _settings = {'user_settings':user_settings(theme, language, notifications)}
    with open(file_name, 'w') as file:
        json.dump(_settings, file, indent=4)


file_name = 'task_3.json'
main(file_name)



# Задача 4
# Найти все данные в задачах со статусом “in_progress” в 'task_4.json' и записать их в отдельный файл любого формата (проще всего в Json формат)


def load_document(file_name):
    with open(file_name) as f:
        text = json.load(f)
        return text['team_tasks']


def find_in_progress_tasks(task_list):
    in_progress_tasks_list = {'unfulfilled tasks': []}
    for task in task_list:
        if task['status'] == 'in_progress':
            in_progress_tasks_list['unfulfilled tasks'].append(task)
    return in_progress_tasks_list


def add_list_for_unfulfilled_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4) 


def main(load_file_name, save_file_name):
    all_tasks = load_document(load_file_name)
    in_progress_tasks_list = find_in_progress_tasks(all_tasks)
    add_list_for_unfulfilled_tasks(in_progress_tasks_list, save_file_name)



load_file_name = 'task_4.json'
save_file_name = 'unfulfilled_tasks.json'

main(load_file_name, save_file_name)




# Задача 5
# Найти стоимость транзакции, которая была сделана раньше всех (можно использовать модуль datetime или его аналоги)
# данные для задачи в файле 'task_5.json'

def load_file(file_name):
    with open(file_name) as file:
        text = json.load(file)
        return text['transactions']


def find_first_transaction(transactions):
    transactions_date = []
    for transaction in transactions:
        transactions_date.append(transaction['date'])
    
    for transaction in transactions:
        if transaction['date'] == min(transactions_date):
            return transaction

file_name = 'task_5.json'
transactions = load_file(file_name)
first_transaction = find_first_transaction(transactions)
for key, value in first_transaction.items():
    print(f'{key}: {value}')

