# Задача 1
# Создайте класс Book, представляющий книгу. 
# Реализуйте магические методы сравнения (==, !=, <, >, <=, >=) на основе сравнения года издания книги.
# Книги сравниваются по году издания.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        return self.year == other.year if isinstance(other, Book) else NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.year < other.year if isinstance(other, Book) else NotImplemented

    def __le__(self, other):
        return self.year <= other.year if isinstance(other, Book) else NotImplemented

    def __gt__(self, other):
        return self.year > other.year if isinstance(other, Book) else NotImplemented

    def __ge__(self, other):
        return self.year >= other.year if isinstance(other, Book) else NotImplemented

# Пример использования:
book1 = Book("Title1", "Author1", 2000)
book2 = Book("Title2", "Author2", 1990)

print(book1 == book2)  # False
print(book1 != book2)  # True
print(book1 < book2)   # False
print(book1 > book2)   # True
print(book1 <= book2)  # False
print(book1 >= book2)  # True