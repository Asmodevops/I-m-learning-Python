import os
from transaction import Transaction
from book import Book
from library import Library
from user import User, create_user

def clear():
    os.system('cls')

library = Library()
book1 = Book('Война и Мир', 'Л.Н. Толстой', '1867', 'Роман', count=6)
book2 = Book('Мастер и Маргарита', 'М.А. Булгаков', '1967', 'Роман', count=31)
book3 = Book('Ромео и Джульетта', 'Уильям Шекспир', '1597', 'Трагедия', count=1)
book4 = Book('Фауст', 'И.В.ф.Гёте', '1808', 'Трагедия', count=3)

library.add_book(book1, book2, book3, book4)
user = User(create_user())
print(f'Добро пожаловать в библиотеку, {user.name}!\n')
while True:
    command = input('''1 - Пользователь
2 - Библиотекарь

0 - Выход
Выбор: ''')
    match command:
        case '0':
            clear()
            print('Всего доброго!')
            break

        case '1':
            clear()
            while True:
                command = input('''1 - Информация о пользователе
2 - Зарегистрироваться в библиотеке
3 - Посмотреть список книг, имеющихся в библиотеке
4 - Взять книгу
5 - Вернуть книгу

0 - Выйти
Выбор: ''')
                match command:
                    case '0':
                        clear()
                        break

                    case '1':
                        clear()
                        user.display_info()
                        print()

                    case '2':
                        clear()
                        library.user_registration(user)

                    case '3':
                        clear()
                        library.show_books()

                    case '4':
                        clear()
                        if user not in library.list_of_users:
                            print('Сначала зарегистрируйтесь в библиотеке.\n')
                            continue

                        library.show_books()
                        print('Укажите порядковый номер книги, которую желаете взять:', end=' ')
                        try:
                            choice = int(input())
                            if choice > len(library.list_of_books) or choice <= 0:
                                clear()
                                print('Следовало указать порядковый номер книги.\n')
                                continue
                            clear()
                            library.give_a_book(library.list_of_books[choice - 1], user)

                        except:
                            clear()
                            print('Следовало указать порядковый номер книги.\n')
                            continue

                    case '5':
                        clear()
                        if not user.books:
                            print('У вас на руках нет ни одной книги.\n')
                            continue

                        books = [book for book in user.books]
                        counter = 1
                        for book in books:
                            print(f'{counter} - Название: {book.name}, Автор: {book.author}.')
                            counter += 1
                        print()
                        print('Укажите порядковый номер книги, которую желаете вернуть:', end=' ')
                        try:
                            choice = int(input())
                            if choice > len(books) or choice <= 0:
                                clear()
                                print('Следовало указать порядковый номер книги.\n')
                                continue
                            clear()
                            library.return_book(books[choice - 1], user)

                        except:
                            clear()
                            print('Следовало указать порядковый номер книги.\n')
                            continue

        case '2':
            clear()
            while True:
                command = input('''1 - Посмотреть список книг в библиотеке
2 - Добавить книгу
3 - Удалить книгу
4 - Посмотреть зарегистрированных пользователей
5 - Посмотреть транзакции пользователя

0 - Выйти
Выбор: ''')
                match command:
                    case '0':
                        clear()
                        break
                    case '1':
                        clear()
                        library.show_books()
                    case '2':
                        name = input('Введите название книги: ')
                        if name.lower() in [book.name.lower() for book in library.list_of_books]:
                            try:
                                clear()
                                count = int(input('Введите количество книг, которое хотите добавить: '))
                                for book in library.list_of_books:
                                    if name.lower() == book.name.lower():
                                        book.count += count
                                        clear()
                                        print('Книги добавлены.\n')
                                continue
                            except:
                                clear()
                                print('Следовало добавить валидное количество книг.\n')
                                continue
                        author = input('Введите данные автора книги: ')
                        year = input('Введите год издания книги: ')
                        genre = input('Введите жанр книги: ')
                        try:
                            count = int(input('Введите количество книг (число): '))
                            books = {}
                            books[len(library.list_of_books)] = Book(name, author, year, genre, count)
                            library.add_book(books[len(library.list_of_books)])
                            clear()
                            print('Книга успешно добавлена в библиотеку.\n')

                        except:
                            clear()
                            print('Следовало добавить валидное количество книг.\n')
                            continue

                    case '3':
                        clear()
                        library.show_books()
                        print('Укажите порядковый номер книги, которую желаете удалить:', end=' ')
                        try:
                            choice = int(input())
                            if choice > len(library.list_of_books) or choice <= 0:
                                clear()
                                print('Следовало указать порядковый номер книги.\n')
                                continue
                            clear()
                            library.deleted_book(library.list_of_books[choice - 1])
                            print('Книга успешно удалена из библиотеки.\n')

                        except:
                            clear()
                            print('Следовало указать порядковый номер книги.\n')
                            continue

                    case '4':
                        clear()
                        if not library.list_of_users:
                            print('В библиотеке еще нет зарегистрированных пользователей.\n')
                            continue

                        for user in library.list_of_users:
                            user.display_info()
                            print()

                        print()

                    case '5':
                        clear()
                        if not library.list_of_users:
                            print('В библиотеке еще нет зарегистрированных пользователей.\n')
                            continue

                        for user in library.list_of_users:
                            user.display_info()
                            print()

                        id = input('Укажите ID пользователя, чьи транзакции желаете посмотреть: ')
                        clear()
                        for user in library.list_of_users:
                            if id == user.id:
                                Transaction.transaction_display(user)

                        print()