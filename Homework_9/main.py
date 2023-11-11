# Задача 1
# написать функцию is_positive(num), которая возвращает True в случае, если num положительное, и False во всех остальных случаях. 
# Дан список чисел (только целые числа).
# Напечатать 0 и отрицательные числа в списке применив, функцию is_positive

def is_positive(num):
    if num > 0:
        return True 
    else:
        return False
    
lst = [3, 2, 1, 0, -1, -2, -3]

for i in lst:
    print(is_positive(i))

input('\nНажмите Enter, чтобы продолжить...\n')

# Задача 2
# Маша хочет удобный калькулятор для вычисления скидки на конфеты.
# Если она покупает до 5 кг конфет, скидки нет
# Если от 5 до 7, то скидка 10%
# Если от 7 и больше, то скидка 25% .
# Реализуйте функция для вычисления скидки, параметры функции слеудет указать самостостоятельно


def discount_calculator(kg):
    if kg <= 0:
        return 'Неверное значение'
    
    elif kg < 5:
        return 0
    elif 5 <= kg <= 7:
        return 10
    elif kg > 7:
        return 25



quantity = float(input('Введите желаем колличество килограмм конфет: '))
price = float(input('Введите стоимость конфет за килограмм: '))

discount = discount_calculator(quantity)

print(f'''
      При покупке {quantity} килограмм конфет стоимостью {price} рублей, скидка составит {discount}%. 
      Выкладывай {(quantity*price) - ((quantity * price) * discount / 100)} рублей.
      ''')

input('Нажмите Enter, чтобы продолжить...\n')


# Задача 3
# написать функцию num_to_name_week(num_day_week), которая возвращает имя дня недели(строка)
# ПРимер 
# num_to_name_week(1) -> ‘Понедельник’

def num_to_name_week(num_day_week):
    days = {
        1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота',
        7: 'Воскресенье'
    }

    if not 1 <= num_day_week <= 7:
        return 'не существует'

    return days[num_day_week]

day_number = 2

print(f'День недели под номером {day_number} - {num_to_name_week(day_number)}.')

input('\nНажмите Enter, чтобы продолжить...\n')


# Задача 4
# написать функцию для фигуры как на картинке: Task_4.png
# и решить задачу с применением этой функции

from turtle import *
from time import sleep


def hexagon():
    speed(75)
    color('blue')
    for i in range(10):
        left(360/10)
        forward(100)
        right(360/10)
        forward(100)
        right(360/10)
        forward(100)
        right(360/10)
        forward(100)
        right((360 - (360/10*6))/2)
        forward(100)
        right(360/10)
        forward(100)
        right(360/10)
        forward(100)
        right(360/10)
        forward(100)


def pentagon():
    speed(75)
    color('red')
    for i in range(10):
        left(360/10)
        forward(200)
        right(360/10*2)
        forward(200)
        right(360/10*2)
        forward(200)
        right(360/10*2)
        forward(200)
        right(360/10*2)
        forward(200)



hexagon()
pentagon()
sleep(5)