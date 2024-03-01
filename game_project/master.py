class Master:
    def __init__(self):
        self.master = 'Хозяин'
        self.money = 100
        self.meat = 0
        self.skin = 0

    def withdraw_money(self, money):
        self.money -= money

    def show_money(self):
        return self.money

    def show_meat(self):
        return self.meat

    def show_skin(self):
        return self.skin

