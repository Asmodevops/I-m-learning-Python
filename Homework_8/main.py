# Задача 1
# используя модуль turtle и создав функцию рисования квадрата, решите следующую задачу: Task_1.png
# *все квадраты одинакового размера  

from turtle import *
from time import sleep

SIDE_LENGTH = 50 # Длина стороны каждого квадратика
SPEED = 75 # Скорость черепашки

def square(side):
    '''Создает один маленький квадратик'''
    speed(SPEED)
    for i in range(4):
        forward(side)
        left(90)

def five_square():
    '''Создает 1 ряд из пяти маленьких квадратиков'''
    for i in range(5):
        square(SIDE_LENGTH)
        penup()
        forward(SIDE_LENGTH)
        pendown()

def all_square():
    '''Создает 5 рядов, в каждом из которых по 5 маленьких квадратиков'''
    for i in range(5):
        if i < 4:
            five_square()
            penup()
            left(180)
            forward(SIDE_LENGTH * 5)
            left(90)
            forward(SIDE_LENGTH)
            left(90)
            pendown()
        else: 
            five_square()


all_square()
sleep(3)
clearscreen()



# Задача 2
# используя модуль turtle и создав функцию рисования квадрата, решите следующую задачу: Task_2.png
# * все треугольники одинакового размера. 

SIDE_LENGTH_TRIANGLE = 113 # Длина стороны каждого треугольника
SPEED_TRIANGLE = 75 # Скорость черепашки

def new_square(side):
    '''Создает квадрат'''
    speed(SPEED_TRIANGLE)
    for i in range(4):
        forward(side)
        left(90)


def plus_triangle():
    '''Рисует треугольники вокруг квадрата'''
    new_square(SIDE_LENGTH_TRIANGLE)
    for i in range(4):
        right(180/3)
        forward(SIDE_LENGTH_TRIANGLE)
        left(180/3*2)
        forward(SIDE_LENGTH_TRIANGLE)
        left(30)


plus_triangle()
sleep(3)
clearscreen()



# Задача 3
# используя модуль turtle и создав функцию рисования шестиугольника, решите следующую задачу: Task_3.png
# * все шестиугольники одинакового размера.

SIDE_LENGTH_HEXAGON = 120 # Длина стороны каждого шестиугольника
SPEED_HEXAGON = 75 # Скорость черепашки

def hexagon(side):
    '''Рисует один шестиугольник'''
    speed(SPEED_HEXAGON)
    for i in range(6):
        left(360/6)
        forward(side)


def all_hexagon():
    '''Рисует три шестиугольника, как на картинке))'''
    for i in range(3):
        hexagon(SIDE_LENGTH_HEXAGON)
        left(360/6)
        penup()
        forward(SIDE_LENGTH_HEXAGON)
        right(180)
        pendown()

all_hexagon()
sleep(3)
bye()



# Задача 4
# создать функцию для генерации списка случайными числами 
import random

def list_of_random_numbers(count, start, end):
    '''Создает список случайных чисел в заданном пользователем диапазоне'''
    for i in range(count):
        random_list.append(random.randint(start, end))


count_of_random_numbers = 10 # Ожидаемое колличество случайных чисел в списке
start_number = 1 # Начальное значение диапазона для формирования случайных чисел
end_number = 100 # Конечное значение диапазона для формирования случайных чисел
random_list = [] # Будущий список случайных чисел

list_of_random_numbers(count_of_random_numbers, start_number, end_number)
print(f'\nВаш список случайных чисел: {random_list}')

input('\nНажмите Enter, чтобы продолжить...')



# Задача 5
# создать функцию для подсчета кол-во упоминаний слова в тексте только для латинского алфавита.
import string
def count_word(text, word):
    '''Функция для подсчета кол-ва упоминаний слова в тексте'''
    text = text.translate(str.maketrans('', '', string.punctuation)).lower() # Удаляем знаки препинания и приводим текст в нижний регистр
    text_list = text.split() # Сплитим текст в список слов
    word = word.lower() # Переводим искомое слово тоже в нижний регистр
    counter = 0 # Создаем переменную для подсчета 
    for i in text_list: # Проходимся циклом по каждому слову в тексте
        if i == word: # сравниваем каждое слово с искомым
            counter += 1 # если они совпадает увеличиваем счетчик на единицу соответственно
    return counter # возвращаем итоговое колличество

s = 'Lorem ipsum dolor sit, sit sit. Sit. SIT, sit, sIt amet.' # Собственно сам текст
word_for_count = 'sIt' # Слово, колличество упоминаний которого будем считать

result = count_word(s, word_for_count)
print(f'\nКолличество слов {word_for_count} в заданном тексте: {result}.')

input('\nНажмите Enter, чтобы продолжить...\n')



# # Задача 6
# # создать функцию для определения четверти по координате точки

def coord(x, y):
    if x == 0 or y == 0:
        return 'Точка лежит на оси.'
    elif x > 0:
        if y > 0:
            return 1
        elif y < 0:
            return 4
    elif x < 0:
        if y > 0:
            return 2
        elif y < 0:
            return 3

x = 1
y = 3
result = coord(x, y)
if type(result) == str:
    print(result)
else:
    print(f'Точка с координатами х: {x}, y: {y} лежит в {result} четверти.')