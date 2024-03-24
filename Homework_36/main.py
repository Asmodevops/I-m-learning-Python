# 1.	Создать  БД “онлайн-магазина,”с таблицами users, orders, products(таблицы можно создать и не через питон) и требования:
# a.	Пользователи могут регистрироваться, входить в систему и изменять свои данные.
# b.	Администратор может добавлять, удалять и изменять информацию о продуктах.
# c.	Пользователи могут просматривать каталог товаров, добавлять их в корзину и оформлять заказы.
# d.	После оформления заказа пользователь должен получить подтверждение по электронной почте.
# e.	Статус заказа должен автоматически изменяться в зависимости от его выполнения (например, "в обработке", "отправлен", "доставлен").


import sqlite3
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Функция для подключения к базе данных SQLite
def connect():
    conn = sqlite3.connect('task_management.db')
    return conn

# Функция для создания таблиц
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'To Do',
        assigned_to INTEGER,
        FOREIGN KEY (assigned_to) REFERENCES users(id)
    )
    ''')

    conn.commit()

# Функция для регистрации нового пользователя
def register(conn, username, password, email):
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, hashed_password, email))
    conn.commit()
    print("Регистрация прошла успешно!")

# Функция для аутентификации пользователя
def login(conn, username, password):
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = cursor.fetchone()
    if user:
        return user[0]  # Возвращаем ID пользователя
    else:
        return None

# Функция для создания новой задачи
def create_task(conn, title, description, assigned_to):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description, assigned_to) VALUES (?, ?, ?)', (title, description, assigned_to))
    conn.commit()
    print("Новая задача успешно создана!")

# Функция для просмотра задач пользователя
def view_tasks(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE assigned_to = ?', (user_id,))
    tasks = cursor.fetchall()
    if tasks:
        print("Ваши задачи:")
        for task in tasks:
            print(f"ID: {task[0]}, Заголовок: {task[1]}, Описание: {task[2]}, Статус: {task[3]}")
    else:
        print("У вас нет назначенных задач.")

# Функция для изменения статуса задачи
def change_task_status(conn, task_id, new_status):
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
    conn.commit()
    print("Статус задачи успешно изменен!")

# Отправка уведомления по электронной почте
def send_email(subject, message, to_email):
    from_email = 'YOUR EMAIL'  # Укажите ваш адрес электронной почты
    password = 'YOUR PASSWORD'  # Укажите ваш пароль

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.yandex.ru', 465)  # Укажите SMTP сервер и порт
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Пример использования функций
if __name__ == '__main__':
    conn = connect()
    create_tables(conn)

    while True:
        print("1. Регистрация")
        print("2. Вход")
        choice = input("Выберите действие: ")

        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            email = input("Введите адрес электронной почты: ")
            register(conn, username, password, email)
        elif choice == '2':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            user_id = login(conn, username, password)
            if user_id:
                print("Вход выполнен успешно!")
                while True:
                    print("1. Создать задачу")
                    print("2. Просмотреть задачи")
                    print("3. Изменить статус задачи")
                    print("4. Выход")
                    user_choice = input("Выберите действие: ")
                    if user_choice == '1':
                        title = input("Введите заголовок задачи: ")
                        description = input("Введите описание задачи: ")
                        create_task(conn, title, description, user_id)
                        send_email("Новая задача", f"Заголовок: {title}, Описание: {description}", email)
                    elif user_choice == '2':
                        view_tasks(conn, user_id)
                    elif user_choice == '3':
                        task_id = int(input("Введите ID задачи: "))
                        new_status = input("Введите новый статус задачи: ")
                        change_task_status(conn, task_id, new_status)
                    elif user_choice == '4':
                        break
            else:
                print("Ошибка: неверное имя пользователя или пароль.")
        else:
            print("Неверный выбор.")
