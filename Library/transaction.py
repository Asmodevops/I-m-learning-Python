# Транзакция
# Свойства: дата, тип(выдача/возврат), книга, пользователь
# Методы: запись транзакции, вывод информации о транзакции
import datetime as dt
import json

class Transaction:
        def __init__(self, type, book, user):
            self.date = ''.join(str(dt.date.today()))
            self.type = type
            self.book = book.name, book.author
            self.user = user.name, user.id

        def display_info(self):
            print(f'Дата: {self.date}, \nТип: {self.type}, \nКнига: {self.book}, \nПользователь: {self.user}.')

        def transaction_record(self):
            transaction = {'Номер транзакции': str(self.transaction_number()),
                           'Дата': self.date,
                           'Тип транзакции': self.type,
                           'Книга': self.book,
                           'Пользователь': self.user}
            try:
                with open('transaction.json', encoding='utf-8') as file:
                    data = json.load(file)
                    file.close()
                    if len(data) == 0:
                        with open('transaction.json', 'a', encoding='utf-8') as f:
                            json.dump([{f'TRANSACTION': transaction}], f, indent=4, ensure_ascii=False)
                    else:
                        data.append(transaction)
                        with open('transaction.json', 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
            except:
                with open('transaction.json', 'a', encoding='utf-8') as f:
                    json.dump([transaction], f, indent=4, ensure_ascii=False)

        @staticmethod
        def transaction_number():
            try:
                with open('transaction.json', encoding='utf-8') as file:
                    return len(json.load(file)) + 1
            except:
                return 1

        @classmethod
        def transaction_display(cls, user):
            try:
                with open('transaction.json', encoding='utf-8') as file:
                    transactions = json.load(file)
                    for transaction in transactions:
                        if user.id in transaction['Пользователь']:
                            print(transaction)
            except:
                print('Транзакции отсутствуют.')

