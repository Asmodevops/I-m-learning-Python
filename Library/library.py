# Библиотека
# Свойства: список книг, список пользователей
# Методы: добавление/удаление книг, регистрация/удаление пользователя, выдача/возврат книги пользователю, вывод списка доступных книг
import json
from transaction import Transaction

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, *books):
        for book in books:
            self.list_of_books.append(book)

    def deleted_book(self, book):
        self.list_of_books.remove(book)

    def user_registration(self, user):
        if user not in self.list_of_users:
            self.list_of_users.append(user)
            print(f'Вы успешно зарегистрировались в библиотеке, {user.name}.\n')
        else:
            print(f'{user.name}, вы уже зарегистрированы в библиотеке.\n')

    def deleted_user(self, user):
        self.list_of_users.remove(user)

    def give_a_book(self, book, user):
        if book.count == 0:
            print('Данные книги закончились.\n')
            return
        if book in user.books:
            print('У вас уже есть такая книга.\n')
            return
        user.take_a_book(book)
        transactions = {}
        transactions[str(transaction_number())] = Transaction('Выдача', book, user)
        transactions[str(transaction_number())].transaction_record()
        book.reduce_books()
        print('Книга выдана.\n')
        return

    def return_book(self, book, user):
        user.return_a_book(book)
        transactions = {}
        transactions[str(transaction_number())] = Transaction('Возврат', book, user)
        transactions[str(transaction_number())].transaction_record()
        book.add_a_book()
        print('Книга возвращена.\n')
        return

    def show_books(self):
        counter = 1
        for book in self.list_of_books:
            print(f'{counter} - {book}')
            counter += 1
        print()

def transaction_number():
    try:
        with open('transaction.json', encoding='utf-8') as file:
            return len(json.load(file)) + 1
    except:
        return 1