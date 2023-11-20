from turtle import *
import numpy
# Задача 1
# Вывести на экран фигуру из звездочек:
# *******
# *******
# *******
# *******
# (квадрат из n строк, в каждой строке n звездочек)
# n - гарантируется, что целое число

print('\nЗадача № 1.\n')
n = int(float(input('Введите длину стороны квадрата из звездочек^^: ')))

if n > 0:
    for i in range(n):
        print("*" * n)

else:
    print('Нельзя вводить число меньше единицы.')


# # Задача 2

# # Дан список элементов 1, 3, 22, 7, 12, 8, 2 (могут быть какие-то другие значения, ввод данных делать не нужно)  

# # 1. показать каждый элемент, последняя цифра которого 2
# # 2. показать произведение чисел, последняя цифра которого 2


print('\nЗадача № 2.\n')

list = [1, 3, 22, 7, 12, 8, 2]

# 1.
new_list = []

for i in list:

    if i < 12 and i == 2 or i >= 12 and i % 10 == 2:
        new_list.append(i)

print(new_list)

# 2.
result = 1

for i in new_list:
    result *= i

print(result)


# # Задача 3
# # распечатайте все числа, которые делятся на 3 от start до end(включительно) 
# # (start, end - могут быть перепутаны), start , end- гарантируется, что целые числа

print('\nЗадача № 3.\n')

end = int(float(input('Задайте 1 число для диапазона: ')))
start = int(float(input('Задайте 2 число для диапазона: ')))

if end < start:
    start, end = end, start

for i in range(start, end+1):
    if i % 3 == 0:
        print(i, end=' ')


# Задача 4
# Напишите программу для черепахи, чтобы она рисовала вот так - Task_4.png (кол-во углов произвольное)
# ВСЕ ЗАДАЧИ С РИСОВАНИЕМ ВЫПОЛНЯТЬ ПРИ КОММЕНТИРОВАНИИ ПРЕДЫДУЩИХ


print('\nЗадача № 4.\n')

corner = int(input('Введите колличество углов для черепашки: '))
side = 10
colors = ['black', 'red', 'blue', 'yellow']

for i in range(corner):
    color(colors[0])
    colors.append(colors[0])
    colors.pop(0)
    left(90)
    forward(side)
    right(90)
    forward(side)
    side += 5

exitonclick()


# Задача 5
# напишите программу для черепахи, чтобы она рисовала вот так - Task_5.png (кол-во сторон произвольное)

print('\nЗадача № 5.\n')

colors = ['red', 'green', 'blue']
 
length = 10
side = int(input('Введите колличество сторон: '))
 
for i in range(side):
    color(colors[0])
    colors.append(colors[0])
    colors.pop(0)
    forward(length)
    left(90)
    length += 10
 
 
exitonclick()


# Задача 6
# напишите программу для черепахи, чтобы она рисовала вот так - Task_6.png (кол-во сторон произвольное)

print('\nЗадача № 6.\n')

colors = ['red', 'black', 'blue']
 
length = 25
side = int(input('Введите колличество сторон: '))
check = 1

for i in range(side):

    match check:

        case 1:
            color(colors[0])
            forward(length)
            left(90)
            check += 1

        case 2:
            forward(length)
            right(90)
            check += 1

        case 3:
            forward(length)
            right(90)
            check += 1

        case 4:
            forward(length)
            left(90)
            colors.append(colors[0])
            colors.pop(0)
            check = 1
 
exitonclick()


# Задача 7
# Выведите на экран числа 1.2, 1.4, 1.6, ..., 2.8. Для программы необходимо использовать цикл for

print('\nЗадача № 7.\n')

end = 3.0
start = 1.2
step = 0.2

for i in numpy.arange(start, end, step):
    print('%.1f' % i, end='  ') # % - здесь используется в качестве оператора форматирования строки. Число после точки (в нашем случае это - 1) означает колличество знаков после запятой. Символ f обозначает тип данных (у нас - float).


# Задача 8
# Дано:
# n - кол-во сторон (гарантируется, что число целое)
# a - сторона многоугольника
# is_fill - нужно залить фигуру (гарантируется, что будет использован только логический тип данных)
# нарисовать ПРАВИЛЬНЫЙ многоугольник по заданным характеристикам 
# УСЛОЖНЕНИЕ(необязательно делать) (добавьте еще одну переменную, хочет ли пользователь, чтобы каждая сторона многоугольника была разного цвета)

print('\n\nЗадача № 8.\n')

n = int(input('Введите колличество сторон для многоугольника: '))
a = int(input('Введите длину стороны многоугольника: '))
is_fil = True
colors = input('Хотите, чтобы каждая сторона многоугольника была разного цвета (да/нет)?').lower()

match colors:
    case 'да':
        colors = ['yellow', 'blue', 'pink', 'orange', 'green']

    case 'нет':
        colors = []

if is_fil:
    begin_fill()
    fillcolor('red')

for i in range(n):
    if colors:
        color(colors[0])
        colors.append(colors[0])
        colors.pop(0)

    forward(a)
    left(360/n)
    
if is_fil:
    end_fill()

exitonclick()