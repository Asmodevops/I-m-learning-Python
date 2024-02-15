# Класс Counterattack: Отвечает за реализацию контратак.
# Включает методы для восстановления прочности и довольства замка или проведения контратаки против противника.
import random


class Counterattack:
    def __init__(self, castle, name, description, health, contentment):
        self._castle = castle
        self.name = name
        self.description = description
        self.health = health
        self.contentment = contentment
        self.cooldown = 0


    def __str__(self):
        return f'{self.description}\nПрочность замка +{self.health}\nДовольство +{self.contentment}'


def counterattack_list_create(counterattacks: list):
    counterattack_list = []
    for counterattack in counterattacks:
        if counterattack.cooldown == 0:
            counterattack_list.append(counterattack)
        else:
            counterattack.cooldown -= 1

    finally_counterattacks = []
    for _ in range(4):
        while True:
            counterattack = random.choice(counterattack_list)
            if counterattack not in finally_counterattacks:
                finally_counterattacks.append(counterattack)
                break
            else:
                continue

    return finally_counterattacks

def counterattack_used(castle, counterattack):
    print('\n' + counterattack.description)
    castle.add_health(counterattack.health)
    castle.add_contentment(counterattack.contentment)
    if counterattack.name == '***ПЕСКИ ВРЕМЕНИ***':
        counterattack.cooldown = -1
        print(f'Прочность замка восстановлена до максимального уровня.\n'
              f'Довольство граждан восстановлено до максимального уровня.\n')
    else:
        counterattack.cooldown = 10
        print(f'Прочность замка: +{counterattack.health}\n'
              f'Довольство граждан: +{counterattack.contentment}\n')