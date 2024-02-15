import random
import json

from castle import Castle, castle_health, castle_contentment
from event import EventGenerator
from counterattack import Counterattack, counterattack_list_create, counterattack_used
import os

def clear():
    """Очистка консоли"""
    os.system('cls')
def create_name():
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']',
               '{', '}', ':', ';', '"', '\'', '\\', '|', '/', '?', '.', '>', ',', '<']
    while True:
        name = input('Введите ваше имя: ')
        if len(name) < 2:
            print('Имя должно состоять из 2-ух и более символов.')
            continue
        if name.isdigit():
            print('Имя не может состоять только из цифр.')
            continue
        if name.isspace():
            print('Имя не может быть пустой строкой.')
            continue
        for symbol in list(name):
            if symbol in symbols:
                print('Имя не должно содержать специальных символов.')
                name = create_name()
        break
    return name.capitalize()

castle = Castle()
random_event = EventGenerator(castle)
counterattacks = []
super_counterattack = Counterattack(castle,
                                    '***ПЕСКИ ВРЕМЕНИ***',
                                    'Вы раскопали в саду древний артефакт, благодаря которому удалось повернуть время вспять и вернуть начальное положение дел.',
                                    health=100,
                                    contentment=100)

with open("counterattack_data.json", encoding='UTF-8') as file:
    data = json.load(file)
for item in data:
    counterattacks.append(Counterattack(castle, item, data[item], random.randint(3, 10), random.randint(3, 10)))
    counterattacks.append(super_counterattack)

print('Добро пожаловать в игру "Защити свой замок"!')
print('Прежде чем продолжить, предлагаю познакомиться!')
user_name = create_name()

clear()
print(f'''{user_name}, добро пожаловать в захватывающий мир "Замковой Защиты"!
Тебя ждут уникальные вызовы и невероятные приключения в роли защитника Замка Лунного Сияния.

Замок Лунного Сияния, где волшебство сочетается с великолепием, стал объектом внимания загадочных сил.
Случайные события, словно порожденные самим волшебством, начали развиваться вокруг.
Твоя задача - предотвратить хаос и сохранить атмосферу веселья.

Замок обладает двумя ключевыми параметрами: прочность и довольство жителей.
Прочность определяет, насколько ваш замок может выдерживать неприятности,
а довольство жителей показывает уровень радости и счастья, царящих в его стенах.
Ваша миссия - умело балансировать между этими параметрами, управлять случайными событиями
и применять контратаки, чтобы Замок Лунного Сияния продолжал сверкать волшебством и весельем.

Приготовьтесь к неожиданным приключениям, встречайте чудеса с улыбкой на лице,
и помните, что именно вы, защитники замка, станете героями этой захватывающей истории.
Вперед, к новым вызовам и защите Замка Лунного Сияния от веселых, но не всегда безобидных, волшебных капризов!\n''')

while True:
    if castle.health == 0 or castle.contentment == 0:
        if castle.health == 0:
            print("\nПрочность замка достигла предела. Замок рушится у вас на глаза. Вы ничего не можете с этим сделать...")
        elif castle.contentment == 0:
            print('\nДовольство жителей достигло нижней планки. Люди больше не любят вас и не доверяют вам. Вы больше не имеете авторитета.')
        print('\nИгра закончена. Вы проиграли.')
        break
    print(castle)
    command = input('''\n1 - Восстановить часть замка
2 - Покормить нуждающихся
3 - Ничего не делать

0 - Выйти
Выбор: ''')
    match command:
        case '0':
            print('\nВсего доброго!')
            break

        case '1':
            if castle.health == 100:
                print('\nРабочие осмотрели замок и, поняв, что им нечего восстанавливать, ушли отдыхать.')
            if castle.health == 99:
                castle_health(castle, 1)
            if castle.health == 98:
                castle_health(castle, random.randint(1,2))
            if castle.health <= 97:
                castle_health(castle, random.randint(1,3))
            chance = random.randint(1,2)
            if chance == 2:
                print()
                random_event.generate_event()
                while True:
                    choice = input('''\n1 - Использовать контратаку
2 - Ничего не делать

Выбор: ''')
                    match choice:
                        case '2':
                            break
                        case '1':
                            counterattack_list = counterattack_list_create(counterattacks)
                            while True:
                                counter = 1
                                for counterattack in counterattack_list:
                                    print(f'{counter} - {counterattack.name}')
                                    print(f'Прочность замка: +{counterattack.health}\n'
                                          f'Довольство граждан: +{counterattack.contentment}\n')
                                    counter += 1

                                counterattack_choice = input('Укажите порядковый номер: ')
                                match counterattack_choice:
                                    case '1':
                                        counterattack_used(castle, counterattack_list[0])
                                        break

                                    case '2':
                                        counterattack_used(castle, counterattack_list[1])
                                        break

                                    case '3':
                                        counterattack_used(castle, counterattack_list[2])
                                        break

                                    case '4':
                                        counterattack_used(castle, counterattack_list[3])
                                        break
                            break

        case '2':
            if castle.contentment == 100:
                print('\nЛюди отказываются брать еду с пола. Их уже ничем не удивишь.')
            if castle.contentment == 99:
                castle_contentment(castle, 1)
            if castle.contentment == 98:
                castle_contentment(castle, random.randint(1,2))
            if castle.contentment <= 97:
                castle_contentment(castle, random.randint(1,3))
            chance = random.randint(1,2)
            if chance == 2:
                print()
                random_event.generate_event()
                while True:
                    choice = input('''\n1 - Использовать контратаку
2 - Ничего не делать

Выбор: ''')
                    match choice:
                        case '2':
                            break
                        case '1':
                            counterattack_list = counterattack_list_create(counterattacks)
                            while True:
                                counter = 1
                                for counterattack in counterattack_list:
                                    print(f'{counter} - {counterattack.name}')
                                    print(f'Прочность замка: +{counterattack.health}\n'
                                          f'Довольство граждан: +{counterattack.contentment}\n')
                                    counter += 1

                                counterattack_choice = input('Укажите порядковый номер: ')
                                match counterattack_choice:
                                    case '1':
                                        counterattack_used(castle, counterattack_list[0])
                                        break

                                    case '2':
                                        counterattack_used(castle, counterattack_list[1])
                                        break

                                    case '3':
                                        counterattack_used(castle, counterattack_list[2])
                                        break

                                    case '4':
                                        counterattack_used(castle, counterattack_list[3])
                                        break
                            break

        case '3':
            print('\nВы прошлись по окрестностям, осмотрели свои владения, полили цветы.\n'
                  'В общем, не сделали ничего полезного.\n')
            chance = random.randint(1,2)
            if chance == 2:
                print()
                random_event.generate_event()
                while True:
                    choice = input('''\n1 - Использовать контратаку
2 - Ничего не делать

Выбор: ''')
                    match choice:
                        case '2':
                            break
                        case '1':
                            counterattack_list = counterattack_list_create(counterattacks)
                            while True:
                                counter = 1
                                for counterattack in counterattack_list:
                                    print(f'{counter} - {counterattack.name}')
                                    print(f'Прочность замка: +{counterattack.health}\n'
                                          f'Довольство граждан: +{counterattack.contentment}\n')
                                    counter += 1

                                counterattack_choice = input('Укажите порядковый номер: ')
                                match counterattack_choice:
                                    case '1':
                                        counterattack_used(castle, counterattack_list[0])
                                        break

                                    case '2':
                                        counterattack_used(castle, counterattack_list[1])
                                        break

                                    case '3':
                                        counterattack_used(castle, counterattack_list[2])
                                        break

                                    case '4':
                                        counterattack_used(castle, counterattack_list[3])
                                        break
                            break