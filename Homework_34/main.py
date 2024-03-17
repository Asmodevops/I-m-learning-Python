import sqlite3 as sq

# Создание соединения с базой данных (файл будет создан, если не существует)
conn = sq.connect('restaurant.db')

# Создание курсора для выполнения операций с базой данных
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''CREATE TABLE IF NOT EXISTS Restaurant
                (id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Tables
                (id INTEGER PRIMARY KEY,
                restaurant_id INTEGER,
                number INTEGER,
                capacity INTEGER,
                FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations
                (id INTEGER PRIMARY KEY,
                table_id INTEGER,
                client_name TEXT,
                reservation_time TEXT,
                FOREIGN KEY (table_id) REFERENCES Tables(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Waiters
                (id INTEGER PRIMARY KEY,
                restaurant_id INTEGER,
                name TEXT,
                FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id))''')

# Вставка тестовых данных
cursor.execute("INSERT OR IGNORE INTO Restaurant (id, name, address, phone) "
               "VALUES (1, 'Restaurant 1', 'Address 1', '123456')")
cursor.execute("INSERT OR IGNORE INTO Restaurant (id, name, address, phone) "
               "VALUES (2, 'Restaurant 2', 'Address 2', '789012')")
cursor.execute("INSERT OR IGNORE INTO Restaurant (id, name, address, phone) "
               "VALUES (3, 'Restaurant 3', 'Address 3', '345678')")
cursor.execute("INSERT OR IGNORE INTO Restaurant (id, name, address, phone) "
               "VALUES (4, 'Restaurant 4', 'Address 4', '901234')")

cursor.execute("INSERT OR IGNORE INTO Tables (id, restaurant_id, number, capacity) "
               "VALUES (1, 1, 1, 4)")
cursor.execute("INSERT OR IGNORE INTO Tables (id, restaurant_id, number, capacity) "
               "VALUES (2, 1, 2, 6)")
cursor.execute("INSERT OR IGNORE INTO Tables (id, restaurant_id, number, capacity) "
               "VALUES (3, 2, 1, 8)")
cursor.execute("INSERT OR IGNORE INTO Tables (id, restaurant_id, number, capacity) "
               "VALUES (4, 3, 1, 4)")
cursor.execute("INSERT OR IGNORE INTO Tables (id, restaurant_id, number, capacity) "
               "VALUES (5, 3, 2, 6)")
cursor.execute("INSERT OR IGNORE INTO Tables (id, restaurant_id, number, capacity) "
               "VALUES (6, 4, 1, 4)")

cursor.execute("INSERT OR IGNORE INTO Reservations (id, table_id, client_name, reservation_time) "
               "VALUES (1, 1, 'John Doe', '2024-03-17 18:00')")
cursor.execute("INSERT OR IGNORE INTO Reservations (id, table_id, client_name, reservation_time) "
               "VALUES (2, 2, 'Jane Smith', '2024-03-17 19:00')")
cursor.execute("INSERT OR IGNORE INTO Reservations (id, table_id, client_name, reservation_time) "
               "VALUES (3, 3, 'Alice Johnson', '2024-03-17 20:00')")

cursor.execute("INSERT OR IGNORE INTO Waiters (id, restaurant_id, name) "
               "VALUES (1, 1, 'Waiter 1')")
cursor.execute("INSERT OR IGNORE INTO Waiters (id, restaurant_id, name) "
               "VALUES (2, 2, 'Waiter 2')")
cursor.execute("INSERT OR IGNORE INTO Waiters (id, restaurant_id, name) "
               "VALUES (3, 3, 'Waiter 3')")
cursor.execute("INSERT OR IGNORE INTO Waiters (id, restaurant_id, name) "
               "VALUES (4, 4, 'Waiter 4')")

# Сохранение изменений
conn.commit()

# Запросы
def execute_query(query):
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# 1. Запрос на получение информации о ресторане
execute_query("SELECT name, address, phone "
              "FROM Restaurant WHERE id = 1")

# 2. Запрос на выборку доступных столов
execute_query("SELECT number, capacity "
              "FROM Tables WHERE restaurant_id = 2")

# 3. Запрос на получение списка бронирований для ресторана
execute_query("SELECT r.id, r.client_name, t.number, r.reservation_time "
              "FROM Reservations r "
              "JOIN Tables t ON r.table_id = t.id "
              "WHERE t.restaurant_id = 3")

# 4. Запрос на получение списка официантов для ресторана
execute_query("SELECT id, name "
              "FROM Waiters WHERE restaurant_id = 4")

# 7. Запрос на получение информации о бронировании по идентификатору
execute_query("SELECT * "
              "FROM Reservations WHERE id = 7")

# 8. Запрос на подсчет количества столов в ресторане
execute_query("SELECT COUNT(*) "
              "FROM Tables WHERE restaurant_id = 4")

# 9. Запрос на выборку столов по вместимости
execute_query("SELECT number, capacity "
              "FROM Tables WHERE capacity >= 6")

# 10. Запрос на поиск информации о клиенте по имени
execute_query("SELECT * FROM Reservations "
              "WHERE client_name LIKE '%John%'")

# Закрытие соединения с базой данных
conn.close()
