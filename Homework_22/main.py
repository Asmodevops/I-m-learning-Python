# Задача 1
# Создать класс "Person" с атрибутами "name", "age", "email" и методами для чтения и записи данных всех трех атрибутов,
# а также реализовать валидацию для атрибута "age":
# ●	должно быть положительным целым числом

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = self.validate_age(age)
        self.email = email

    @staticmethod
    def validate_age(age):
        if type(age) != int:
            raise 'age must be int'
        
        if age <= 0:
            raise 'age must be a positive number'
        
        return age
    
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_age(self):
        return self.age
    
    @property
    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = self.validate_age(age)

    def set_email(self, email):
        self.email = email



person_1 = Person('Rustam', 26, 'admasdh@mail.ru')
print('Исходный экземпляр класса:')
print(person_1.get_name)
print(person_1.get_age)
print(person_1.get_email)

print('\nИзменим имя:')
person_1.set_name('Oleg')
print(person_1.get_name)
print(person_1.get_age)
print(person_1.get_email)

print('\nИзменим возраст:')
person_1.set_age(15)
print(person_1.get_name)
print(person_1.age)
print(person_1.get_email)

print('\nИзменим email:')
person_1.set_email('ooooooooo@yandex.ru')
print(person_1.get_name)
print(person_1.age)
print(person_1.get_email)



# Задача 2
# Создать класс "Product" с атрибутами "name", "price", "quantity" и методами для чтения и записи данных всех трех атрибутов, 
# а также реализовать валидацию для атрибута "price":
# ●	должно быть положительным целым или дробным числом

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = self.validate_price(price)
        self.quantity = quantity

    @staticmethod
    def validate_price(price):
        if type(price) != int and type(price) != float:
            raise 'price must be int or float'
        
        if price <= 0:
            raise 'price must be a positive number'
        
        return price
    
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_price(self):
        return self.price
    
    @property
    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = self.validate_price(price)

    def set_quantity(self, quantity):
        self.quantity = quantity



product_1 = Product('Pen', 45, 10000)
print('\n\nИсходный экземпляр класса:')
print(product_1.get_name)
print(product_1.get_price)
print(product_1.get_quantity)


print('\nИзменим название товара:')
product_1.set_name('Pineapple')
print(product_1.get_name)
print(product_1.get_price)
print(product_1.get_quantity)


print('\nИзменим цену товара:')
product_1.set_price(155)
print(product_1.get_name)
print(product_1.get_price)
print(product_1.get_quantity)

print('\nИзменим количество товара:')
product_1.set_quantity(555)
print(product_1.get_name)
print(product_1.get_price)
print(product_1.get_quantity)

