import functools
import random
import re

# Задача 1
# Дана произвольная строка создать строку, в которой содержаться только цифры из исходной строки

# Пример:
#   Ввод:
#   АА”АА324А К*К№5 10 79

#   Вывод:
#   32451079

string = 'АА”АА324А К*К№5 10 79'
reg_exp = '\d'
string = ''.join(filter(lambda num: re.fullmatch(reg_exp, num), string))
print(string)

input('\nЧтобы продолжить, нажмите Enter...')


# Задача 2
# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Необходимо создать новый список чисел, которые будут составлять 70% от исходного числа. Для создания такого списка использовать функцию map().
# Необходимо посчитать разницу между суммами исходного списка и преобразованного
# ПРИМЕР
# ввод
# 100, 50, 30 (сумма 180)
# 70, 35, 21 (сумма 126)

# вывод
# 54


func_for_random_numbers = [lambda: random.randint(1, 100) for i in range(10)]
list_numbers = [func() for func in func_for_random_numbers]

new_list_numbers = list(map(lambda num: int(num * 0.7), list_numbers))
result = functools.reduce(lambda result, num: result + num, list_numbers) - functools.reduce(lambda result, num: result + num, new_list_numbers)
print(f'\nИзначальный список: {list_numbers}')
print(f'Новый список, в котором числа составляют 70% от исходного: {new_list_numbers}')
print(f'Разница между суммами исходного и преобразованного списков: {result}.')

input('\nЧтобы продолжить, нажмите Enter...')


# Задача 3
 
# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Создать новый список при помощи filter(), отобрать значения по маске 3*3? , где * - любое кол-во цифр, ? - одна цифра
# Вычислить при помощи reduce() произведение нового списка
# Пример работы маски:
#   Даны числа:
#       31139
#       339
#       1339
#       33
#   Вывод:
#       31139
#       339


lst_nums = [31139, 339, 1339, 33, 333, 3434, 343]
print(f'\nДан список: {lst_nums}')


reg_exp = '3\d{0,}3\d{1}'
new_lst_nums = list(map(lambda string: str(string), lst_nums))
new_lst_nums = list(filter(lambda num: re.fullmatch(reg_exp, num), new_lst_nums))
new_lst_nums = list(map(lambda num: int(num), new_lst_nums))
print(f'Отфильтрованный список по маске, согласно условиям задачи: {new_lst_nums}')
result = functools.reduce(lambda result, num: result * num, new_lst_nums)

print(f'Произведение чисел нового списка: {result}')

