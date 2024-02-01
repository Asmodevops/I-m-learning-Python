# Задача 
# Разработайте систему классов для управления рестораном. 
# Создайте базовый класс "Блюдо" с общими характеристиками (например, название, цена). 
# Затем создайте подклассы для различных типов блюд, таких как "Завтрак" и "Ужин", добавляя специфичные свойства и методы. 
# Реализуйте метод для расчета общей стоимости заказа.

class Dish:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = self.is_valid_price(price)
    
    def is_valid_price(self, price):
        if type(price) not in (int, float):
            raise 'Type price must be int or float'
        return price
    

class Breakfast(Dish):
    def __init__(self, name, price, has_coffee: bool):
        super().__init__(name, price)
        self.has_coffee = has_coffee

    def display_info(self):
        print(f"{self.name} - ${self.price}{' with coffee' if self.has_coffee else ''}")


class Dinner(Dish):
    def __init__(self, name, price, has_dessert: bool):
        super().__init__(name, price)
        self.has_dessert = has_dessert

    def display_info(self):
        print(f"{self.name} - ${self.price}{' with dessert' if self.has_dessert else ''}")

class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def calculate_total(self):
        total_cost = 0
        for dish in self.dishes:
            total_cost += dish.price
        return total_cost

# Пример использования:

# Создаем блюда
breakfast1 = Breakfast("English breakfast", 15, True)
dinner1 = Dinner("Grilled Chicken", 13, False)
dinner2 = Dinner("Pasta Bolognese", 18, True)

# Создаем заказ
order = Order()

# Добавляем блюда в заказ
order.add_dish(breakfast1)
order.add_dish(dinner1)
order.add_dish(dinner2)

# Выводим информацию о заказе
for dish in order.dishes:
    dish.display_info()

# Рассчитываем и выводим общую стоимость заказа
total_cost = order.calculate_total()
print(f"\nTotal Cost: ${total_cost}")