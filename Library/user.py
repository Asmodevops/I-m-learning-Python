# Пользователем
# Свойства: имя, айди, список взятых книг
# Методы: вывод информации о пользователе, взятие /возврат книг


class User:
    def __init__(self, name):
        self.name = name
        self.id = self.add_id()
        self.books = []

    @staticmethod
    def add_id():
        id = create_id()
        try:
            with open('id_list.txt', 'r') as file:
                read_file = file.readline()
                file.close()
                while id in read_file:
                    id = create_id()
        except:
            with open('id_list.txt', 'w') as file:
                file.close()

        with open('id_list.txt', 'a') as file:
            file.write(f'{id}\n')
        return id


    def display_info(self):
        print(f'Имя: {self.name}, '
              f'ID: {self.id}')
        if self.books:
            print('Книги на руках: ')
            counter = 1
            for book in self.books:
                print(f'{counter}) Название: {book.name}, Автор: {book.author}.')
                counter += 1

    def take_a_book(self, book):
        self.books.append(book)

    def return_a_book(self, book):
        self.books.remove(book)


def create_id():
    import random
    import string
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    return id


def create_user():
    print('Чтобы воспользоваться библиотекой скажите, как я могу к вам обращаться?')
    name = input()
    return name