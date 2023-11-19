# Задача 1
# Сделайте функцию, которая параметром будет принимать букву и проверять, это буква кириллицы или латиницы.

def language_check(letter):
    en = 'ABCDEFGHIYKLMNOPQRSTUVWXYZ'
    ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if letter.upper() in en:
        return 'Это буква латиницы.'
    elif letter.upper() in ru:
        return 'Это буква кириллицы.'
    else:
        return 'Полагаю, что это не буква.'
    
s = input('Введите букву: ')
if 0 < len(s) < 2:
    result = language_check(s)
    print(result)
else:
    print('Надо бы ввести букву. ОДНУ. Не две не три. ОДНУ.')

input('Нажмите Enter, чтобы продолжить...')



# Задача 2
# Найти ошибку(и)
# функция calc(a, b, operation). Описание входных параметров:
# 1. Первое число
# 2. Второе число
# 3. Действие над ними:
#    1) + Сложить
#    2) - Вычесть
#    3) * Умножить
#    4) / Разделить
#    5) В остальных случаях функция должна возвращать "Операция не поддерживается"

def calc(a, b, operation):
    # лоовим возможную ошибку при вводе данных, например строкового значения
    try:
        result = 'Операция не поддерживается'

        if operation == '+':
            # Исключаем конкатенацию
            if type(a) == str and type(b) == str:
                result = 'Не число!' 
            else:
                result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            # Исключаем умножение строки
            if type(a) == str or type(b) == str:
                result = 'Не число!' 
            else:
                result = a * b
        elif operation == '/':
            # Проверка деления на ноль
            if b != 0:
                result = a / b
            else:
                result = 'Деление на 0!'

        # Возвращаем результат выполнения функции
        return result
    
    # В случае если допущена ошибка. Возвращаем результат указывающий на неверные входные параметры.
    except:
        result = 'Не число!'
        return result



# Проверяем корректные значения
print(f"\nВходные значения: 30 + 15\nОжидаемый результат = 45 \nФактический результат: {calc(30, 15, '+')}") 
print(f"\nВходные значения: 30 - 15\nОжидаемый результат = 15 \nФактический результат: {calc(30, 15, '-')}") 
print(f"\nВходные значения: 30 * 15\nОжидаемый результат = 450 \nФактический результат: {calc(30, 15, '*')}") 
print(f"\nВходные значения: 30 / 4\nОжидаемый результат = 7.5 \nФактический результат: {calc(30, 4, '/')}") 

# Проверяем проверку деления на ноль
print(f"\nВходные значения: 30 / 0\nОжидаемый результат = 'Ошибка деления на 0!' \nФактический результат: {calc(30, 0, '/')}") 

# Проверяем неподдерживаемую операцию
print(f"\nВходные значения: 30 % 15\nОжидаемый результат = 'Неподдерживаемая операция.' \nФактический результат: {calc(30, 15, '%')}") 

# Проверяем неверные входные данные
print(f"\nВходные значения: 'тридцать' + 15\nОжидаемый результат = 'Сообщение об ошибке.' \nФактический результат: {calc('тридцать', 15, '+')}") 
print(f"\nВходные значения: 30 + 'пятнадцать'\nОжидаемый результат = 'Сообщение об ошибке.' \nФактический результат: {calc(30, 'пятнадцать', '+')}") 

# Проверяем возможную конкатенацию
print(f"\nВходные значения: 'тридцать' + 'пятнадцать'\nОжидаемый результат = 'Сообщение об ошибке.' \nФактический результат: {calc('тридцать', 'пятнадцать', '+')}") 

# Проверяем возможное умножение строки 
print(f"\nВходные значения: 'тридцать' * 15\nОжидаемый результат = 'Сообщение об ошибке.' \nФактический результат: {calc('тридцать', 15, '*')}") 
print(f"\nВходные значения: 30 * 'пятнадцать'\nОжидаемый результат = 'Сообщение об ошибке.' \nФактический результат: {calc(30, 'пятнадцать', '*')}") 



