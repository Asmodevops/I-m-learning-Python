import re
# Задача 1
# Дана произвольная строка.
# Написать регулярное выражение для поиска в строке серии и номера паспорта 
# Допускается только запись паспорта из предложенных ниже: 
# 00 00 000000
# или 00 00 000 000
# или 00-00-000-000
# или 00-00-000000
# на месте 0 может стоять любая цифра 
# ((Программа должны вывести кол-во валидных значений и показать их в консоле )
# или 
# (напишите алгоритм в текстовом варианте, что нужно сделать ))

passport = '''
Валидные значения:
11 11 111111
22 22 222 222
33-33-333-333
44-44-444444


Невалидные значения:
5555 666666
7777 777 777
8888-888888
9999-999-999'''


reg_exp = "(\d{2}[\s|-]\d{2}[\s|-](\d{6}|\d{3}[\s|-]\d{3}))"
result = re.findall(reg_exp, passport)

valid_values = []

for i in range(len(result)):
    for j in result[i]:
        if len(j) == 12 or len(j) == 13:
            valid_values.append(j)

print(valid_values)

input('\nНажмите Enter, чтобы продолжить...\n')


# Задача 2
# Дана строка с произвольная строка  

# написать регулярное выражение для определения номера автомобиля. 
# Допускается только такая запись номера автомобиля А000АА
# А-любая буква(латиница)
# 0-любая цифра

# ((Программа должны вывести кол-во валидных значений и показать их в консоле )
# или 
# (напишите алгоритм в текстовом варианте, что нужно сделать ))

auto_numbers = '''
Валдиные значения:
A000AA
B555DC
T345PX
M109ET

Невалидные значения:
a555AA
A555Aa
A555aA
a555aa
a555aA
a555Aa
A555aa
'''

reg_exp_for_auto_numbers = "[A-Z]\d{3}[A-Z][A-Z]"
valid_auto_numbers = re.findall(reg_exp_for_auto_numbers, auto_numbers)
print(valid_auto_numbers)
