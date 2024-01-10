from reservation import Reservation
from rooms import get_rooms, choice_room
from date_check import valid_start_date, valid_end_date
from name_check import is_valid_name



# Задача 1
# Реализуйте класс для управления системой бронирования отелей. 
# Класс Бронь должен содержать информацию о госте, дате заезда и выезда, типе номера. 
# Методы должны позволять бронировать, отменять бронь и проверять доступность номеров на определенные даты.


while True:
    command = input(
'''
1 - Забронировать номер;
2 - Отменить бронь;

0 - Выход.
''')
    match command:
        case '0':
            print('Всего Доброго!')
            break
        case '1':
            print('Какой номер хотели бы забронировать?')
            room_type = choice_room(get_rooms())
            while room_type == False:
                print('Выбран неверный номер. Попробуйте еще раз.')
                room_type = choice_room(get_rooms())

            start_date = input('Введите дату заезда (в формате: гггг-мм-дд): ')
            while valid_start_date(start_date) != True:
                print('\nВведена неверная дата. Попробуйте еще раз.') 
                start_date = input('Введите дату заезда (в формате: гггг-мм-дд): ')
            
            end_date = input('Отлично! Теперь введите дату выезда (в формате: гггг-мм-дд): ')
            while valid_end_date(start_date, end_date) != True:
                print('\nВведена неверная дата. Попробуйте еще раз.') 
                end_date = input('Введите дату выезда (в формате: гггг-мм-дд): ')
            
            first_name = input('Введите ваше имя: ').capitalize()
            while is_valid_name(first_name) != True:
                print('\nВведите достоверные данные.')
                first_name = input('Введите ваше имя: ').capitalize()
            last_name = input('Введите вашу фамилию: ').capitalize()
            while is_valid_name(last_name) != True:
                print('\nВведите достоверные данные.')
                last_name = input('Введите ваше имя: ').capitalize()
            reservation = Reservation(first_name, last_name, start_date, end_date, room_type)
            reservation.add_reservation()

        case '2':
            print('Чтобы отменить бронь, для начала выберите номер, который вы бронировали.')
            room_type = choice_room(get_rooms())
            while room_type == False:
                print('Выбран неверный номер. Попробуйте еще раз.')
                room_type = choice_room(get_rooms())

            start_date = input('Введите дату заезда (в формате: гггг-мм-дд): ')
            while valid_start_date(start_date) != True:
                print('\nВведена неверная дата. Попробуйте еще раз.') 
                start_date = input('Введите дату заезда (в формате: гггг-мм-дд): ')
            
            end_date = input('Отлично! Теперь введите дату выезда (в формате: гггг-мм-дд): ')
            while valid_end_date(start_date, end_date) != True:
                print('\nВведена неверная дата. Попробуйте еще раз.') 
                end_date = input('Введите дату выезда (в формате: гггг-мм-дд): ')
            
            first_name = input('Введите ваше имя: ').capitalize()
            while is_valid_name(first_name) != True:
                print('\nВведите достоверные данные.')
                first_name = input('Введите ваше имя: ').capitalize()
            last_name = input('Введите вашу фамилию: ').capitalize()
            while is_valid_name(last_name) != True:
                print('\nВведите достоверные данные.')
                last_name = input('Введите ваше имя: ').capitalize()
            del_reservation = Reservation(first_name, last_name, start_date, end_date, room_type)
            del_reservation.del_reservation()

        case _:
            pass



# Задача 2
# Класс Книга должен содержать информацию о названии, авторе и жанре книги.

class Book:
    def __init__(self, name: str, author: str, genre: str):
        self.name = name
        self.author = author
        self.genre = genre

    def show_book(self):
        print(
f'''
Название: {self.name},
Автор: {self.author}
Жанр: {self.genre}
''')

book_1 = Book('Триумфальная арка', 'Эрих Мария Ремарк', 'Роман')
book_1.show_book()
book_2 = Book('Вино из одуванчиков', 'Рэй Брэдбери', 'Роман')
book_2.show_book()



