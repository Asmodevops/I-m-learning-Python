import re
from random import randint as rd

# Задача 1
# Дан текстовый файл. В каждой строке написано имя и возраст в таком формате “Иван: 20”. 
# Найти имя человека и его возраст, который младше всех, а также найти имя и возраст человека, который старше всех

with open('task_1.txt', 'r', encoding='utf-8') as task_1:
    task_1 = task_1.readlines()

task_1 = list(map(lambda names: names.strip(), task_1))

# Вариант 1
print('Вариант 1:')
for i in range(len(task_1)-1):
    for j in range(len(task_1)-1):
        if int(task_1[j][(task_1[j].find(':'))+2:]) > int(task_1[j+1][task_1[j+1].find(':')+2:]):
            task_1[j], task_1[j+1] = task_1[j+1], task_1[j]

print('Младше всех:')
print(task_1[0])
for i in range(1, len(task_1)):
    if int(task_1[i][task_1[i].find(':')+2:]) == int(task_1[0][task_1[0].find(':')+2:]):
        print(task_1[i])

print('\nСтарше всех:')
print(task_1[len(task_1)-1])
for i in range(len(task_1)-2, 0, -1):
    if int(task_1[i][task_1[i].find(':')+2:]) == int(task_1[-1][task_1[-1].find(':')+2:]):
        print(task_1[i])

# Вариант 2

print('\nВариант 2:')
facebook = {}
for i in range(len(task_1)):
    if int(task_1[i][task_1[i].find(':')+2:]) not in facebook:
        facebook[int(task_1[i][task_1[i].find(':')+2:])] = [task_1[i][:task_1[i].find(':')]]

    else:
        facebook[int(task_1[i][task_1[i].find(':')+2:])] += [task_1[i][:task_1[i].find(':')]]

facebook = dict(sorted(facebook.items()))

print('Младше всех:')
print(*min(facebook.items()))

print('\nСтарше всех:')
print(*max(facebook.items()))


input('\nНажмите Enter, чтобы продолжить...\n')


# Задача 2
# Дан текстовый файл. в каждой строки записаны email. Найти все невалидные email. email  адрес считает валидным, если содержит “@” и точку после “@”, также его длина должна быть больше 5 символов


with open('task_2.txt', 'r') as task_2:
    task_2 = task_2.readlines()

reg_exp = '^[a-zA-Z0-9._%+-]{5,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
task_2 = list(filter(lambda valid_email: re.findall(reg_exp, valid_email), list(map(lambda email: email.strip(), task_2))))

print('Валидные email:\n', '\n'.join(i for i in task_2), sep='')

input('\nНажмите Enter, чтобы продолжить...\n')


# Задача 3
# Дан текстовый файл. в каждой строки записаны 3 числа - это размеры коробки (длина ширина высота).
# найти коробку:
# 1.	самую длинную 
# 2.	самую широкую 
# 3.	самую узкую (по длине и ширине)
# 4.	самую высокую 
# 5.	наибольшую по объему

def random_boxes(file_path):
    with open(file_path, 'w') as file:
        for i in range(10):
            file.write(f'{rd(1, 100)} {rd(1, 100)} {rd(1, 100)}\n')
    return file_path


def read_boxes(task_3):
    with open(task_3, 'r') as file:
        lines = file.readlines()
    return [tuple(map(int, line.strip().split())) for line in lines]


def find_boxes_properties(boxes):
    longest_box = max(boxes, key=lambda x: x[0]) # Самая длинная коробка
    widest_box = max(boxes, key=lambda x: x[1]) # Самая широкая коробка
    narrowest_box = min(boxes, key=lambda x: (x[0], x[1])) # Самая узкая коробка
    tallest_box = max(boxes, key=lambda x: x[2]) # Самая высокая коробка
    max_volume_box = max(boxes, key=lambda x: x[0] * x[1] * x[2]) # Наибольшая по объему коробка

    return {
        'Самая длинная коробка': longest_box,
        'Самая широкая коробка': widest_box,
        'Самая узкая коробка': narrowest_box,
        'Самая высокая коробка': tallest_box,
        'Наибольшая по объему коробка': max_volume_box
    }


task_3 = random_boxes('task_3.txt')
boxes_data = read_boxes(task_3)
result = find_boxes_properties(boxes_data)

for i, j in result.items():
    print(f'{i}: {j}')
