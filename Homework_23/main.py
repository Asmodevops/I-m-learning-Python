# Задача
# Определите класс Task с атрибутами title и status (например, "в процессе" или "завершено") и методом display_info(), который выводит информацию о задаче.
# Создайте дочерний класс AssignedTask, который наследует от класса Task. Добавьте атрибут assignee (назначенный сотрудник) и метод assign_task(employee), который принимает объект сотрудника и назначает ему задачу.

# Пример использования:
# # Создание объектов
# task1 = Task("Complete report", "в процессе")
# task2 = AssignedTask("Code review", "ожидает", None)
# # Вызов методов
# task1.display_info()  # Выводит информацию о задаче
# employee1 = User("Alice")
# task2.assign_task(employee1)  # Назначение задачи сотруднику
# task2.display_info()  # Выводит информацию о задаче, включая назначенного сотрудника


class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def display_info(self):
        print(f"Task: {self.title}, Status: {self.status}")


class AssignedTask(Task):
    def __init__(self, title, status, assignee):
        super().__init__(title, status)
        self.assignee = assignee

    def assign_task(self, employee):
        self.assignee = employee

    def display_info(self):
        assignee_info = f", Assignee: {self.assignee.name}" if self.assignee else ""
        print(f"Task: {self.title}, Status: {self.status}{assignee_info}")


class User:
    def __init__(self, name):
        self.name = name


# Пример использования
task1 = Task("Complete report", "в процессе")
task2 = AssignedTask("Code review", "ожидает", None)

task1.display_info()

employee1 = User("Alice")
task2.assign_task(employee1)

task2.display_info()