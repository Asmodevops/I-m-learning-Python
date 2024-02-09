from rabbit import Rabbit

def buy_rabbit():
    return Rabbit()

def sell_rabbit(coefficient):
    if coefficient == 1:
        return 10
    else:
        return 7.5 * coefficient * 1.1

def sell_meats(meats):
    return 5 * meats

def sell_skins(skins):
    return 10 * skins