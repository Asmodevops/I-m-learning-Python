class Cell:
    def __init__(self):
        self.lvl = 1
        self.place = 5
        self.feeder = 20
        self.max_feeder = 20
        self.drinking_bowl = 20
        self.max_drinking_bowl = 20
        self.rabbits = []
        self.exp = 0
        self.amount_exp = 10

    def add_exp(self):
        self.exp += 1
        if self.exp == int(self.amount_exp):
            self.lvl_up()


    def lvl_up(self):
        self.lvl += 1
        if self.lvl in [2, 3, 4, 5, 7, 10, 14, 19, 25]:
            self.place += 1

        self.max_feeder += 10
        self.max_drinking_bowl += 10
        self.exp = 0
        self.amount_exp *= 1.5




    def add_rabit(self, *rabbits):
        if len(self.rabbits) < self.place:
            for rabbit in rabbits:
                self.rabbits.append(rabbit)
                print('Кролик уже ждет тебя в клеточке.')
        else:
            print('В клетке больше нет места 😢')
            return


    def __str__(self):
        return (f'Уровень клетки: {self.lvl}, '
                f'Кролики: {len(self.rabbits)}/{self.place}, '
                f'Кормушка: {self.feeder}/{self.max_feeder}, '
                f'Поилка: {self.drinking_bowl}/{self.max_drinking_bowl}, '
                f'Экспа: {self.exp}/{int(self.amount_exp)}.')


