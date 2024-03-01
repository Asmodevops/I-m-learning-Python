class Rabbit:
    def __init__(self):
        self.sex = self.add_sex()
        self.name = self.add_name(self)
        self.breed = self.add_breed()
        self.health = 100
        self.lvl = 1
        self.exp = 0
        self.max_exp = 10

    @staticmethod
    def add_sex():
        import random
        sex = ['Мальчик', 'Девочка']
        return random.choice(sex)

    @staticmethod
    def add_breed():
        import random
        breeds = ['Черно-бурый',
                  'Серебристый',
                  'Белый великан',
                  'Бабочка',
                  'Венский голубой',
                  'Венский белый',
                  'Венский черный',
                  'Русский горностаевый',
                  'Советский мардер',
                  'Аляска',
                  'Голландский',
                  'Калифорнийская']
        return random.choice(breeds)

    @staticmethod
    def add_name(self):
        import random
        female_names = ['бубочка', 'зефирка', 'кексик', 'пуся', 'манюня', 'кисточка', 'бусинка']
        male_names = ['чупик', 'чаёк', 'кубик', 'бантик', 'бурёк', 'венцеслав', 'пуля']
        if self.sex == 'Мальчик':
            return random.choice(male_names).capitalize()
        else:
            return random.choice(female_names).capitalize()

    def add_max_exp(self):
        self.max_exp = self.lvl * 10

    def __str__(self):
        return (f'Имя: {self.name}, '
                f'Пол: {self.sex}, '
                f'Порода: {self.breed}, '
                f'Жизики: {self.health}, '
                f'Уровень: {self.lvl}, '
                f'Экспа: {self.exp}/{self.max_exp}.')


    def rename(self, new_name):
        if type(new_name) is not str:
            print('Не называй кроликов как попало. Они заслуживают твоего уважения.')
            return 0
        if new_name == '':
            print('Кролики - не пустое место. Не называй их так.')
            return 0
        if new_name.isdigit():
            print('Дурацкое имя. Придумаешь другое - приходи.')
            return 0
        if new_name.isspace():
            print('Ну ты себя пустой строчкой назови.')
            return 0
        name_splited = list(new_name)
        forbidden_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                             '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                             '-', '_', '=', '+', '.', ',', '?', '/', '|', ' ', '\\']
        for symbol in forbidden_symbols:
            if symbol in name_splited:
                print('Нормальное имя сделай. Не дуркуй.')
                return 0

        self.name = new_name.capitalize()
        print(f'Кролик был переименован. Мои поздравления.')
        return 50

class Dead_rabbit(Rabbit):
    def __init__(self, name):
        self.name = name
        self.status = 'дохлый'

    def __str__(self):
        return f'Имя: {self.name}, {self.status} 😭'