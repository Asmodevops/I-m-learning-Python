# Задача 1: Управление банковским счетом
# Реализуйте класс BankAccount, который представляет банковский счет.
# Класс должен содержать атрибуты balance (баланс) и методы deposit (положить деньги на счет)
# и withdraw (снять деньги со счета). Создайте собственный класс исключения InsufficientFundsError,
# который будет возбуждаться при попытке снятия суммы, превышающей текущий баланс.

class InsufficientFundsError(Exception):
    """Исключение, возникающее при попытке снятия суммы превышающей текущий баланс."""
    pass


class BankAccount:
    def __init__(self, balance=0):
        """Инициализация банковского счета с указанным начальным балансом."""
        self.balance = balance

    def deposit(self, amount):
        """Положить деньги на счет."""
        if amount < 0:
            raise ValueError("Amount should be positive")
        self.balance += amount
        print(f"Депозит в размере {amount} успешно выполнен. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        """Снять деньги со счета."""
        if amount < 0:
            raise ValueError("Amount should be positive")

        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств на счете.")

        self.balance -= amount
        print(f"Снятие средств в размере {amount} успешно выполнено. Текущий баланс: {self.balance}")


# Пример использования
try:
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  # Этот вызов должен вызвать исключение InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")
except ValueError as e:
    print(f"Ошибка: {e}")



# Задача 2: Работа с файлами
# Реализуйте класс FileManager, представляющий управление файлами.
# Класс должен содержать методы read_file и write_file, которые будут читать данные из файла и
# записывать данные в файл соответственно. Создайте собственный класс исключения FileNotFoundError,
# который будет возбуждаться, если файл не может быть найден при чтении или записи.


class FileNotFoundError(Exception):
    """Исключение, возникающее при попытке работы с файлом, который не существует."""
    pass

class FileManager:
    def read_file(self, filename):
        """Читает данные из файла и возвращает их."""
        try:
            with open(filename, 'r') as file:
                data = file.read()
                print(f"Данные из файла '{filename}':\n{data}")
                return data
        except IOError:
            raise FileNotFoundError(f"Файл '{filename}' не найден.")

    def write_file(self, filename, data):
        """Записывает данные в файл."""
        try:
            with open(filename, 'w') as file:
                file.write(data)
                print(f"Данные успешно записаны в файл '{filename}'.")
        except IOError:
            raise FileNotFoundError(f"Файл '{filename}' не найден.")

# Пример использования
try:
    file_manager = FileManager()

    # Попытка чтения из несуществующего файла
    file_manager.read_file("nonexistent_file.txt")

    # Попытка записи в несуществующий файл
    file_manager.write_file("nonexistent_file.txt", "Пример данных для записи.")
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
