# Задача 1
# Дан текстовый файл. В каждой строке написано дата(формата 10.10.2020) и через “:” выручка. 
# создать “итоговая выручка.txt” и записать выручка за все даты

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as task_1:
        lines = task_1.readlines()
    
    return [list(line.strip().split()) for line in lines]

def total_revenue(file):
    result = 0
    for i in file:
        result += int(i[1])
    return result

def main_task_1():
    file_for_task_1 = 'task_1.txt'
    file = read_file(file_for_task_1)
    total = total_revenue(file)
    with open('Итоговая выручка.txt', 'w', encoding='utf-8') as f:
        text = f'Выручка за все даты: {total}'
        f.write(text)

    print('Выручка за все даты успешно посчитана.')

main_task_1()

input('\nЧтобы продолжить, нажмите Enter...\n')



# Задача 2
# Дан текстовый файл. В каждой строке, которого записано новое слово. Все слова должны быть уникальными(проверку для файла делать не стоит). Пользователь вводит слова. 
# Записывать слова, которые вводит пользователь файл. 

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return list(map(lambda line: line.strip(), lines))


def add_word(file_path, file):
    word = input('Введите ваше слово: ').capitalize()
    with open(file_path, 'a+', encoding='utf-8') as f:
        if word not in file:
            text = '\n' + word
            f.write(text)
            print('Слово успешно добавлено.')
        else:
            print('Данное слово уже имеется в нашем файле.')


def print_words(file):
    for word in file:
        print(word)


def menu():
    print('''
        1. Добавить слово в файл;
        2. Показать все слова в файле;
        
        0. Завершить работу.
        ''')


def main_task_2():
    task_2 = 'task_2.txt'
    choice = None

    while choice != '0':
        file = read_file(task_2)
        menu()
        choice = input('Ваш выбор: ')

        match choice:
            case '0': 
                print('До свидания.')

            case '1':
                add_word(task_2, file)
            
            case '2':
                print_words(file)
                    
            case _:
                print('Такого выбора вам не предоставлено.')

main_task_2()

input('\nЧтобы продолжить, нажмите Enter...\n')



# Задача 3
# Дан текстовый файл. В каждой строке, которого записана дата. Реализовать проверку на валидность даты. Записать валидные даты в файл valid_date.txt
# невалидные даты в файл “none_valid_date.txt”


from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False

def main_task_3():
    file_path = 'task_3.txt'
    valid_file_path = 'valid_date.txt'
    invalid_file_path = 'none_valid_date.txt'

    with open(file_path, 'r') as file, \
         open(valid_file_path, 'w') as valid_file, \
         open(invalid_file_path, 'w') as invalid_file:

        for line in file:
            date_string = line.strip()

            if is_valid_date(date_string):
                valid_file.write(date_string + '\n')
            else:
                invalid_file.write(date_string + '\n')

    print("Проверка завершена. Валидные даты записаны в файл valid_date.txt, невалидные даты записаны в файл “none_valid_date.txt")

main_task_3()