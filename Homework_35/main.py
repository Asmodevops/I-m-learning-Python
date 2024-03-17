import sqlite3 as sq


# Функция для создания таблицы "Студенты"
def create_table():
    connection = sq.connect('students.db')  # Подключение к базе данных (если нет, то создается новая)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                      ID INTEGER PRIMARY KEY,
                      Name TEXT,
                      Surname TEXT,
                      Age INTEGER,
                      GroupName TEXT
                      )''')
    connection.commit()
    connection.close()


# Функция для добавления новой записи в таблицу "Студенты"
def add_student(name, surname, age, group):
    connection = sq.connect('students.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Students (Name, Surname, Age, GroupName) 
                      VALUES (?, ?, ?, ?)''', (name, surname, age, group))
    connection.commit()
    connection.close()
    print("Студент добавлен успешно.")


# Функция для получения данных от пользователя через CLI
def get_input():
    name = input("Введите имя студента: ")
    surname = input("Введите фамилию студента: ")
    age = int(input("Введите возраст студента: "))
    group = input("Введите группу студента: ")
    return name, surname, age, group


# Основная функция программы
def main():
    create_table()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить студента")
        print("2. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            name, surname, age, group = get_input()
            add_student(name, surname, age, group)
        elif choice == "2":
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
