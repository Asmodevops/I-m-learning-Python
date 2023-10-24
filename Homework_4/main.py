import random

# Задача 1
# дан  список
# запрещено использовать sort, max, map преобразовывать список в другие типы тоже нельзя
# найти минимальный элемент в списке
print('\nЗАДАЧА 1\n')

lst = []

for i in range(7):
    lst.append(random.randint(0, 100))

# ------------------------- Решение № 1 -----------------------------

print('\nРешение № 1\n')

print(f'Полный список: {lst}')
print(f'Минимальный элемент в списке: {min(lst)}')

input('\nНажмите Enter, чтобы продолжить...')

# ------------------------- Решение № 2 -----------------------------

print('\nРешение № 2\n')

print(f'Полный список: {lst}')

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(f'Минимальный элемент в списке: {lst[0]}')

input('\nНажмите Enter, чтобы продолжить...')

# ------------------------- Решение № 3 -----------------------------

print('\nРешение № 3\n')

print(f'Полный список: {lst}')

result = lst[0]

for i in lst:
    if result > i:
        result = i

print(f'Минимальный элемент в списке: {result}')

input('\nНажмите Enter, чтобы продолжить...')


# Задача 2
# дан  список
# запрещено использовать sort, max, count, map преобразовывать список в другие типы тоже нельзя
# найти элемент(ы) в списке, который повторяется дважды и более раз

print('\nЗАДАЧА 2\n')

lst_2 = []

for i in range(10):
    lst_2.append(random.randint(1,7))

_lst_unique = []
_lst_not_unique = []

for i in lst_2:
    if i not in _lst_unique:
        _lst_unique.append(i)
    else:
        if i not in _lst_not_unique:
            _lst_not_unique.append(i)

print(f'Ваш список: {lst_2}')
print(f'Повторяемые числа в вашем списке: {_lst_not_unique}.')

input('\nНажмите Enter, чтобы продолжить...')


# Задача 3
# дан  список
# запрещено использовать sort, max, count, sum, map
# сформировать новый список, с положительными числами

print('\nЗАДАЧА 3\n')

lst_3 = []

for i in range(15):
    lst_3.append(random.randint(-100,100))

_lst_positive = []

for i in lst_3:
    if i > 0:
        _lst_positive.append(i)

print(f'Ваш список: {lst_3}')
print(f'Список положительных чисел из вашего списка: {_lst_positive}')

input('\nНажмите Enter, чтобы продолжить...')


# Задача 4
# дан  список
# запрещено использовать sort, max, count, sum, map
# удалить из этого списка, все отрицательные элементы

print('\nЗАДАЧА 4\n')

lst_4 = []

for i in range(15):
    lst_4.append(random.randint(-100,100))

print(f'Ваш список: {lst_4}')

i = 0

while i < len(lst_4):
    if lst_4[i] < 0:
        lst_4.pop(i)
    else:
        i += 1

print(f'Из вашего списка удалили все отрацительные элементы, получился: {lst_4}')

input('\nНажмите Enter, чтобы продолжить...')


# Задача 5
# дан  список
# найти все элементы в этом списке, из которых извлекается квадратный корень в виде целого числа (4, 16 и т.д.)

print('\nЗАДАЧА 5\n')

lst_5 = [86, 41, 72, 12, 64, 16, 89, 81, 51, 88, 69, 44, 54, 5, 70]

_lst_square = []

for i in lst_5:
    if int(i**0.5)**2 == i:
        _lst_square.append(i)

print(f'Ваш список: {lst_5}')
print(f'Элементы вашего списка, из которых извлекается квадратный корень в виде целого числа: {_lst_square}')

input('\nНажмите Enter, чтобы продолжить...')


# Задача 6
# дан  список
# найти  все элементы в этом списке , у которых индекс и значение совпадают. Исходный список нельзя менять 

print('\nЗАДАЧА 6\n')

lst_6 = [11, 2, 12, 4, 1, 14, 4, 13, 8, 9, 2, 4, 8, 4, 5]

_lst_equal_to_index = []

for i in range(len(lst_6)):
    if i == lst_6[i]:
        _lst_equal_to_index.append(lst_6[i])


print(f'Ваш список: {lst_6}')
print(f'Элементы вашего списка, совпадающие со значением индекса: {_lst_equal_to_index}')

input('\nНажмите Enter, чтобы продолжить...')


# Задача 7
# дан  список
# запрещено использовать sort, max, count, sum, map , преобразовывать список в другие типы тоже нельзя
# найти произведение всех элементов в этом списке

print('\nЗАДАЧА 7\n')

lst_7 = []

for i in range(7):
    lst_7.append(random.randint(1,10))

product = 1

for i in lst_7:
    product *= i

print(f'Ваш список: {lst_7}')
print(f'Произведение всех элементов вашего списка равно: {product}')