from get_snowflake_shapes import get_shape
from add_size import choice_size
from add_shape import choice_shape


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
    

    def change_size(self, new_size):
        self.size = new_size
    
    
    def change_shape(self, new_shape):
        self.shape = new_shape


    def add_snowflake(self):
        snowflake = {
            'Размер': self.size, 
            'Форма': self.shape, 
        }

        return snowflake


shapes = get_shape()
print('Задайте размер снежинки: ', end='')
size = choice_size()

print('\nТеперь выберите форму снежинки из списка: ')
shape = choice_shape(shapes)
snowflake = Snowflake(size, shapes[shape])
print('\nСнежинка создана!')


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
            shape = choice_shape(shapes)
            snowflake = Snowflake(size, shapes[shape])
            print('\nСнежинка создана!')


        case '2':
            print('\nВаша снежинка:')
            for key, value in snowflake.add_snowflake().items():
                print(f'    {key}: {value}')


        case '3':
            print('Задайте новый размер для вашей снежинки: ', end='')
            size = choice_size() 
            snowflake.change_size(new_size=size)
            print('\nРазмер снежинки успешно изменен.')

        case '4':
            print('Выберите для вашей снежинки новую форму: ')
            shape = choice_shape(shapes)
            snowflake.change_shape(new_shape=shapes[shape])
            print('\nФорма снежинки успешно изменена.')

        case _:
            pass

