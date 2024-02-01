# Написать программу для управления списком контактов.
# В качестве примера, добавьте в программу два объекта
# Contact в список контактов
# Так же необходимо выполнить операции по удалению
# контакта и поиску контакта в списке (удаление и поиск
# осуществляется пользователем)
# Результаты операций должны выводятся на экран.



class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone_number = phone

    def display_info(self):
        print(f'Name: {self.name}, Phone number: {self.phone_number}.')


class BusinessContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'Company: {self.company}')


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} removed successfully.")
                return
        print(f"Contact {name} not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Contact found:")
                contact.display_info()
                return
        print(f"Contact {name} not found.")

    def show_contacts(self):
        for contact in self.contacts:
            contact.display_info()




phone_book = PhoneBook()

contact1 = Contact("Иван Иванов", "999-999-99-99")
contact2 = BusinessContact("Рустам Насибулин", "999-888-77-77", "МВД России")

phone_book.add_contact(contact1)
phone_book.add_contact(contact2)

phone_book.show_contacts()
print('------------------------------------------------------------------------')
phone_book.search_contact("Рустам Насибулин")
print('------------------------------------------------------------------------')
phone_book.remove_contact("Иван Иванов")
print('------------------------------------------------------------------------')
phone_book.show_contacts()

