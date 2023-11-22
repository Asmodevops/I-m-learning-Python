import random


def print_matrix(matrix):
    for i in matrix:
        print(i)


# Задача 1
# Дана матрица. Вывести на экран первый и последний столбцы.

print('Задача 1.\n')

matrix = [[1, 0, 0, 0, 0, 0, 2], 
          [1, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 2]]

print('Матрица: ')

print_matrix(matrix)

print('\nПервый и последний столбцы матрицы: ')

for i in matrix:
    print(i[0], i[-1])

input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 2
# Дана матрица. Вывести на экран первую и последнюю строки.

print('Задача 2.\n')

matrix = [[1, 1, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [2, 2, 2, 2, 2, 2, 2]]

print('Матрица: ')

print_matrix(matrix)

print('\nПервая и последняя строки: \n', matrix[0], '\n', matrix[-1], sep='')
    

input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 3
# Дан двухмерный массив n×m элементов. Определить, сколько раз встречается число 7 среди элементов массива.

print('Задача 3.\n')

N = 7
M = 7

func_for_matrix = [lambda: random.randint(5,7) for i in range(M)]
matrix = [[func() for func in func_for_matrix] for i in range(N)]

result = 0

for i in matrix:
    for j in i:
        if j == 7:
            result += 1

print('Матрица: ')
print_matrix(matrix)
print(f'\nКолличество цифр 7 среди элементов массива: {result}')

input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 4
# Дана квадратная матрица. Вывести на экран элементы, стоящие на побочной диагонали.

print('Задача 4.\n')

N = 5
M = 5

matrix = [[i for i in range(M)] for j in range(N)]

print('Матрица: ')
print_matrix(matrix)
print('\nЭлементы побочной диагонали: ')

for i in range(len(matrix)):
    print(matrix[i][-1-i], end=' ')

print('\n\nДля наглядности закрасим побочную диагональ звездочками:')

for i in range(len(matrix)):
    matrix[i][-1-i] = '*'
print_matrix(matrix)


input('\nЧтобы продолжить нажмите Enter...\n')



# Задача 5
# Дана матрица. Вывести k-ю строку и p-й столбец матрицы.

print('Задача 5.\n')

matrix = [[1, 2, 3, 4, 5, 6],
          [2, 3, 4, 5, 6, 7],
          [3, 4, 5, 6, 7, 8],
          [4, 5, 6, 7, 8, 9],
          [5, 6, 7, 8, 9, 0]]

k = 5
p = 6

print('Матрица: ')
print_matrix(matrix)

if 0 < k <= len(matrix):
    print(f'\n{k}-я строка матрицы: {matrix[k-1]}.')
else:
    print(f'\n{k}-я строка в матрице отсутствует.')

if 0 < p <= len(matrix[0]):
    print(f'\n{p}-й столбец матрицы: ')
    for i in matrix:
        print('  ->', i[p-1])
else:
    print(f'\n{p}-й столбец в матрице отсутствует.')


input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 6
# Дана матрица размера m x n. Вывести ее элементы в следующем порядке: первая строка справа налево, вторая строка слева направо, третья строка справа налево и так далее.

print('Задача 6.\n')

N = 7
M = 7

matrix = [[i for i in range(N)] for j in range(M)]

print('Матрица: ')
print_matrix(matrix)

print('\nПервая строка справа налево, вторая строка слева направо, третья строка справа налево и так далее:')

for i in range(len(matrix)):
    if i % 2 == 0:
        print(matrix[i][::-1])
    else:
        print(matrix[i])

input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 7
# Создать матрицу, состоящую из нулей, за исключением элементов, которые находятся в крайних столбцах и строках - они равны единице.

print('Задача 7.\n')

length = 10
width = 7

func_for_matrix = [lambda: 0 for i in range(length)]
matrix = [[func() for func in func_for_matrix] for i in range(width)]

for i in range(len(matrix[0])):
    matrix[0][i] = 1
    matrix[-1][i] = 1

for i in range(len(matrix)):
    matrix[i][0] = 1
    matrix[i][-1] = 1
 
print('Матрица: ')
print_matrix(matrix)

input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 8
# Сформировать квадратную матрицу n x n, на диагонали которой находятся случайные числа из диапазона [1; 9], а остальные числа равны 1.

print('Задача 8.\n')

length = 7
width = 7

func_for_matrix = [lambda: 1 for i in range(length)]
matrix = [[func() for func in func_for_matrix] for i in range(width)]


for i in range(len(matrix)):
    matrix[i][-1-i] = random.randint(2,9)
    matrix[i][i] = random.randint(2,9)

print('Матрица: ')
print_matrix(matrix)

input('\nЧтобы продолжить нажмите Enter...\n')


# Задача 9
# Создать квадратную матрицу, на диагонали которой находятся тройки, выше диагонали находятся двойки, остальные элементы равна единице.

print('Задача 9.\n')

N = 7

matrix = [[1] * N for i in range(N)]

for i in range(N):
    matrix[i][-i-1] = 3

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 3:
            matrix[i][j] = 2
        else:
            break
        
print('Матрица: ')
print_matrix(matrix)

input('\nЧтобы продолжить нажмите Enter...\n')

# Задача 10
# Заполнить матрицу так, чтобы сумма элементов в каждой строке была равна номеру этой строки.

print('Задача 10.\n')

length = 5
width = 7

func_for_matrix = [lambda: 0 for i in range(length)]
matrix = [[func() for func in func_for_matrix] for i in range(width)]

for i in range(len(matrix)):
    while sum(matrix[i]) != i + 1:
        for j in range(len(matrix[i])):
            if sum(matrix[i]) == i + 1:
                break
            else:
                matrix[i][j] += 1

print('Матрица: ')
print_matrix(matrix)