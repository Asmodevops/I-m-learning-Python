import json
from get_snowflake_shapes import get_shape
from add_size import choice_size
from add_shape import choice_shape
from save_snowflake import save_snowflake

# Задача 1
# Реализовать класс
# 	Класс Snowflake
# ●	Атрибуты: размер, форма.
# ●	Методы: change_size(new_size), change_shape(new_shape).
# ●	НЕОБЯЗАТЕЛЬНО: Интерфейс для изменения размера и формы снежинки


class Snowflake:
    def __init__(self, size: float, shape: str):
        self.size = size
        self.shape = shape


    def add_snowflake(self):
        snowflake = {
            'Размер': self.size, 
            'Форма': self.shape, 
        }

        return snowflake
    
shapes = get_shape()

while True:
    choice = input(
'''
1 - Создать новую снежинку
2 - Посмотреть снежинку
3 - Изменить размеры снежинки
4 - Изменить форму снежинки

0 - Выход
''')
    
    match choice:
        case '0':
            print('Всего доброго!')
            break

        case '1':
            print('Задайте размер снежинки: ', end='')
            size = choice_size()
            
            print('\nТеперь выберите форму снежинки из списка: ')
            # shapes = get_shape()
            shape = choice_shape(shapes)
            save_snowflake(Snowflake, size, shapes, shape)
            print('Снежинка создана!')

        case '2':
            try:
                with open('snowflake.json', encoding='utf-8') as file:
                    snowflake = json.load(file)
                    for key, value in snowflake.items():
                        print(f'{key}: {value}')


            except (FileNotFoundError, json.JSONDecodeError):
                print('Снежинка еще не создана.')

        case '3':
            try:
                with open('snowflake.json', encoding='utf-8') as f:
                    snowflake = json.load(f)
                
                for key, value in shapes.items():
                    if snowflake['Форма'] == value:
                        shape = key
                print('Задайте новый размер для вашей снежинки: ', end='')
                size = choice_size()
                
                save_snowflake(Snowflake, size, shapes, shape)
                print('Размер снежинки успешно изменен.')

            except (FileNotFoundError, json.JSONDecodeError):
                print('Снежинка еще не создана.')

        case '4':
            try:
                with open('snowflake.json', encoding='utf-8') as f:
                    snowflake = json.load(f)
                size = snowflake['Размер']
                
                print('Выберите для вашей снежинки новую форму: ')
                shape = choice_shape(shapes)
                save_snowflake(Snowflake, size, shapes, shape)
                print('Форма снежинки успешно изменена.')

            except (FileNotFoundError, json.JSONDecodeError):
                print('Снежинка еще не создана.')

        case _:
            pass

