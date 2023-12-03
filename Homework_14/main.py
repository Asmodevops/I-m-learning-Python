# Задача 1
# Среди элементов с нечетными номерами найдите наибольший элемент массива, который делится на 3.

def find_max_dividend(arr):
    max_dividend = 0
    for i in range(len(arr)):
        if arr[i] % 3 == 0:
            if arr[i] > max_dividend:
                max_dividend = arr[i]
    return max_dividend

# Задача 2
# Дан массив и число p. Найдите два различных числа в массиве, сумма которых наиболее близка к p.

def find_max_sum(arr, p):
    a = arr[0]
    b = arr[0]
    max_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if p >= arr[i] + arr[j] > max_sum and i != j and arr[i] != arr[j]:
                a = arr[i]
                b = arr[j]
                max_sum = arr[i] + arr[j]
    return a, b

# Задача 3
# Дан массив. Найдите два соседних элемента, сумма которых минимальна.

def min_sum(arr):
    a = 0
    b = 2
    min_sum = sum(arr[a:b])
    result = arr[a:b]
    while b < len(arr) + 1:
        if min_sum > sum(arr[a:b]):
            min_sum = sum(arr[a:b])
            result = arr[a:b]

        a += 1
        b += 1
    return result

# Задача 4
# Дан массив. Найдите три последовательных элемента в массиве, сумма которых максимальна.

def max_three_number_sum(arr):
    a = 0
    b = 3
    max_sum = sum(arr[a:b])
    result = arr[a:b]
    while b < len(arr) + 1:
        if max_sum < sum(arr[a:b]):
            max_sum = sum(arr[a:b])
            result = arr[a:b]

        a += 1
        b += 1
    return result



lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25] # ожидается ответ 21
print(f'Массив: ', *lst)
print(f'Наибольший элемент массива, который делится на 3: {find_max_dividend(lst)}')
input('\nPress Enter to continue...\n')

lst = [0, 2, 3, 4, 5, 6, 8, 9, 10, 13, 13]
P = 26

print(f'Массив: ', *lst)
print(f'Два числа в массиве, сумма которых наиболее близка к P: {find_max_sum(lst, P)}.')
input('\nPress Enter to continue...\n')


lst = [0, 3, 1, 2, 3, 4, 5, 6, 7, 1, 0, 2, 3, 4, 1, 2, 3]

print(f'Массив: ', *lst)
print(f'Два соседних элемента, сумма которых минимальна: ', end='')
print(*min_sum(lst), sep=', ')

print(f'Три последовательных элемента в массиве, сумма которых максимальна: ', end='')
print(*max_three_number_sum(lst), sep=', ')



