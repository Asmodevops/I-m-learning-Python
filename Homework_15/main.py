# Задача 1
# Дан текстовый файл. Посчитать кол-во букв в файле.
import string
with open('task_1.txt', 'r', encoding='utf-8') as task_1:
    text = task_1.read()

text = ''.join(text.split())
text = text.translate(str.maketrans('', '', string.punctuation))
print(f'Количество букв в файле "task_1.txt": {len(text)}.')

input('Нажмите Enter, чтобы продолжить...')


# Задача 2
# Дан текстовый файл. Написать функцию, которая будет подсчитывать количество чисел в строке,
# которые отделены пробелами, возвращаемое значение должно быть типа int. 
# Применить эту функцию для файла и найти общее кол-во таких чисел

def find_numbers(_str):
    counter = 0
    for item in _str.split():
        try:
            int(item)
            counter += 1
        except:
            pass
    return counter

with open('task_2.txt', 'r', encoding='utf-8') as task_2:
    text = task_2.read()

result = find_numbers(text)
print(f'Количество чисел в файле "task_2.txt": {result}. Тип возвращаемого значения: {type(result)}.')

input('Нажмите Enter, чтобы продолжить...')


# Задача 3
# Дан текстовый файл. Написать функцию, которая составляет шифр для цифр (шифр можете придумать свой, вот пример 1 → ! | 2 → @  | 3 → #  |  4 → $  и т.д.), возвращаемое значение должно быть типа string.
# Применить эту функция для файла и заменить все цифры на зашифрованные значения

def cipher(txt):
    cipher_dict = {
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '&',
        '8': '*',
        '9': '(',
        '0': ')'
    }
    result = ''
    for item in txt:
        if item in cipher_dict:
            result += cipher_dict[item]
        else:
            result += item
    return result

with open('task_3.txt', 'r') as task_3:
    text = task_3.read()

result = cipher(text)
print(result, type(result), sep='\n')

input('Нажмите Enter, чтобы продолжить...')



# Задача 4

# Дан текстовый файл. Написать функцию, которая ищет упоминание о файле формата .txt. Функция должна возвращать имя такого файла без пробелов и вместе с расширением .txt. 
# Применить эту функция для файла и создать список с именами файлов 

import re


def find_txt_files(text):
    reg_exp = r"\b\w+\.txt\b"
    return re.findall(reg_exp, text)


with open('task_4.txt', 'r') as task_4:
    text = task_4.read()


print(find_txt_files(text))
