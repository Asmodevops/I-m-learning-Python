# Книга
# Свойства: название, автор, год издания, жанр, количество экземпляров
# Методы: вывод информации о книге, уменьшение/увеличение количества книг

class Book:
    def __init__(self, name, author, year, genre, count):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.count = count

    def __str__(self):
        return (f'Название: {self.name}, '
                f'Автор: {self.author}, '
                f'Год издания: {self.genre}, '
                f'Жанр: {self.genre}, '
                f'Количество экземпляров: {self.count}.')

    def add_a_book(self):
        self.count += 1

    def reduce_books(self):
        self.count -= 1

