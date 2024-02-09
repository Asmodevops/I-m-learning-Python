# Симулятор фермы кроликов
# В начале игры у вас есть клетка и 100 денюжек.
# Изначально клетка 1 уровня. В ней есть 5 мест для кроликов, поилка и кормушка.
# На старте игры у вас нет кроликов. Поэтому поспешите в магазин и купите их себе.
# При покупке кролики сразу попадают в клетку.
# Также в магазине можно продать своих кроликов. Также можно продать шкурки и мяско.
# Шкурки и мяско добываются в мясоцехе. Убейте своего кролика, чтобы получить с него мяско и шкурку.
# Количество получаемого мяска зависит от уровня кролика. Шкурка достается всегда одна.
# Кроликов можно разводить в кролеспальне. Учтите, что у вас в клетке должен быть кролик мальчик и кролик девочка.
# Скрещивание происходит с определенным шансом. Не всегда все получается с первого раза.
# При успешном скрещивании кролик попадает в клетку. Поэтому имейте в виду, что в клетке должно быть место.
# У каждого кролика есть свой уровень, жизики, пол, порода, а также имя.
# Все кролики получаются с рандомными свойствами.
# Однако в кролепаспортном столе вы можете дать свое имя для вашего кролика. Но услуга не бесплатна, учтите.
# Для того, чтобы кролики повышали свой уровень, вам нужно чилить.
# Чил - это своего рода какой-то промежуток времени.
# Имейте в виду, что пока вы чилите - ваши кролики живут, а значит кушают и пьют водичку.
# Если кормушка опустеет, а поилка высохнет, то жизики кроликов стремительно будут заканчиваться.
# Если у кролика закончатся жизики, то кролик умрет. Мертвый кролик тоже занимает место в клетке.
# Чтобы избавиться от мертвых кроликов, проследуйте в мясоцех. Однако, с мертвого кролика вы получите только шкурку.
# Логично, что мяско с мертвого кролика будет не совсем здоровым.
# Каждый раз, когда кролик повышает свой уровень, качается ваша клетка.
# С повышением уровня клетки, у вас становится больше места в поилке и кормушке.
# Также добавляются места для кроликов. Выше уровень клетки = больше кроликов. Больше кроликов = больше кушают и пьют.

import random
import shop

from rabbit import Rabbit, Dead_rabbit
from cell import Cell
from master import Master

def line():
    print('---------------------------------------------------------------------------------')

cell = Cell()
master = Master()

while True:
    print('--------------------------------------МЕНЮ---------------------------------------')
    command = input('''
1 - Кролеферма 🐇
2 - Сходить в магазин 🏪
3 - Заглянуть в инвентарь 🎒
4 - Чилить 🤤

0 - Закончить игру\nВыбор: ''')
    match command:
        case '0': # Закончить игру
            print('До свидания!')
            break

        case '1': # Посмотреть клетку
            while True:
                print('------------------------------------КЛЕТКА---------------------------------------')
                print(cell)
                print('---------------------------------------------------------------------------------')
                cell_command = input('''
1 - Посмотреть кроликов 🐇
2 - Пополнить кормушку 🥕
3 - Подлить водички 💧
4 - Кролеспальня 💖 
5 - Мясоцех😲
6 - Кролепаспортный стол ⭐
0 - Вернуться в главное меню\nВыбор: ''')
                match cell_command:
                    case '0':
                        break
                    case '1':
                        if len(cell.rabbits) > 0:
                            print('------------------------------------КРОЛИКИ--------------------------------------')
                            counter = 1
                            for rabbit in cell.rabbits:
                                print(f'{counter}) {rabbit}')
                                counter += 1
                        else:
                            line()
                            print('У тебя еще нет кроликов... Покупай скорее.')
                    case '2':
                        if cell.feeder < cell.max_feeder:
                            cell.feeder = cell.max_feeder
                            line()
                            print('Кормушка пополнена. Молодец. Кролики любят кушать.')
                        else:
                            line()
                            print('Кого ты пополнять тут собрался? Кормушка и так полная.')
                    case '3':
                        if cell.drinking_bowl < cell.max_drinking_bowl:
                            cell.drinking_bowl = cell.max_drinking_bowl
                            line()
                            print('Поилка пополнена. Здорово. Без водички и ты помрешь.')
                        else:
                            line()
                            print('Ну ты шо, краёв не видишь? Поилка и так полная. Куда ты льёшь?')
                    case '4':
                        if len(cell.rabbits) < cell.place:
                            if not(Rabbit in [type(rabbit) for rabbit in cell.rabbits]):
                                line()
                                print('Все твои кролики дохлые. Кого ты собрался разводить?')
                            elif len(cell.rabbits) == 0:
                                line()
                                print('Кого ты собрался скрещивать? У тебя еще нет кроликов.')
                            elif len(cell.rabbits) == 1:
                                line()
                                print('У тебя всего один кролик. Что ты собрался с ним делать? Даже не думай!!!')
                            else:
                                male_rabbits = []
                                female_rabbits = []
                                for rabbit in cell.rabbits:
                                    if type(rabbit) is not Dead_rabbit:
                                        if rabbit.sex == 'Мальчик':
                                            male_rabbits.append(rabbit)
                                        else:
                                            female_rabbits.append(rabbit)
                                if len(male_rabbits) == 0:
                                    line()
                                    print('У тебя нет кроликов мальчиков. Что ты собрался делать?')
                                elif len(female_rabbits) == 0:
                                    line()
                                    print('У тебя нет кроликов девочек. Что ты собрался делать?')
                                else:
                                    print('---------------------------------КРОЛЕСПАЛЬНЯ------------------------------------')
                                    male_rabbit = random.choice(male_rabbits)
                                    female_rabbit = random.choice(female_rabbits)
                                    print(f'''{male_rabbit.name} и {female_rabbit.name} просили оставить их одних.
    Не будем им мешать...''')
                                    chance = random.randint(1, 3)
                                    if chance == 3:
                                        new_rabbit = Rabbit()
                                        print('На свет появился новый кролик. Ты только погляди на него: ')
                                        print(new_rabbit)
                                        cell.add_rabit(new_rabbit)
                                    elif chance != 3:
                                        print('Скрещивание не удалось. Приходи в другой раз 🙄')
                        else:
                            line()
                            print('В клетке больше нет места. Никаких скрещиваний!')
                    case '5':
                        if len(cell.rabbits) == 0:
                            line()
                            print('У тебя еще нет кроликов, а ты уже решил их покромсать? Ты изверг.')
                        else:
                            print('------------------------------------МЯСОЦЕХ--------------------------------------')
                            print('Ты решил покромсать своих кроликов? Туда их! Мясо и шкурки сами себя не добудут.\n')
                            while True:
                                counter = 1
                                for rabbit in cell.rabbits:
                                    print(f'{counter}) {rabbit}')
                                    counter += 1
                                choice = input('''\nОт кого хочешь избавиться?
Чтобы вернуться назад введите "0". 
Укажи порядковый номер: ''')
                                if choice == '0':
                                    break
                                try:
                                    choice = int(choice)
                                    if choice > len(cell.rabbits) or choice <= 0:
                                        line()
                                        print('Укажи порядковый номер кролика!')
                                        continue
                                    else:
                                        rabbit = cell.rabbits[choice-1]
                                        cell.rabbits.pop(choice-1)
                                        line()
                                        print(f'{rabbit.name} был(а) жестоко зарезан(а). 😭')
                                        if type(rabbit) is Rabbit:
                                            meat = random.randint(rabbit.lvl, rabbit.lvl * 2)
                                            master.meat += meat
                                            master.skin += 1
                                            print(f'''Шкурки +1, 
Мяско +{meat}.''')
                                            break
                                        else:
                                            master.skin += 1
                                            print(f'''Шкурки +1.''')
                                            break
                                except:
                                    line()
                                    print('Укажи порядковый номер кролика!')

                    case '6':
                        print('--------------------------------КРОЛЕПАСПОРТНЫЙ СТОЛ----------------------------------')
                        if len(cell.rabbits) == 0:
                            print('У тебя еще нет кроликов. Кого ты собрался переименовывать?')
                            continue
                        if not(Rabbit in [type(rabbit) for rabbit in cell.rabbits]):
                            print('Все твои кролики дохлые. Кого ты собрался переименовывать?')
                            continue
                        print('Услуги кролепаспортного стола стоят 50 денюжек. А что? Времена сейчас тяжелые...')
                        while True:
                            command = input('''1 - Воспользоваться услугами кролепаспортного стола
0 - Уйти.\nВыбор:''')
                            match command:
                                case '0':
                                    line()
                                    print('Ну и иди. Жлоб.')
                                    break
                                case '1':
                                    if master.money < 50:
                                        line()
                                        print(f'Если ты забыл, то я тебе напомню: у тебя всего {master.money} денюжек.'
                                              f'Иди давай, поднакопи сначала.')
                                        continue
                                    else:
                                        line()
                                        while True:
                                            counter = 1
                                            rabbits = []
                                            for rabbit in cell.rabbits:
                                                if type(rabbit) is not Dead_rabbit:
                                                    rabbits.append(rabbit)
                                            for rabbit in rabbits:
                                                print(f'{counter}) {rabbit}')
                                                counter += 1
                                            line()
                                            choice = input('''Кого будем переименовывать?
Чтобы вернуться назад введите "0". 
Укажи порядковый номер: ''')
                                            if choice == '0':
                                                break
                                            try:
                                                choice = int(choice)
                                                if choice > len(rabbits) or choice <= 0:
                                                    line()
                                                    print('Укажи порядковый номер кролика!')
                                                    continue
                                                else:
                                                    rabbit = rabbits[choice - 1]
                                                    new_name = input('Теперь введи новое имя для кролика: ')
                                                    line()
                                                    money = rabbit.rename(new_name)
                                                    master.money -= money
                                                    break
                                            except:
                                                line()
                                                print('Укажи порядковый номер кролика!')
                                        break







        case '2': # Сходить в магазин
            while True:
                print('------------------------------------МАГАЗИН--------------------------------------')
                shop_command = input('''
1 - Купить кролика
2 - Продать кролика
3 - Продать мяско
4 - Продать шкурки

0 - Уйти домой\nВыбор: ''')
                match shop_command:
                    case '0':
                        break
                    case '1':
                        while True:
                            rabbit = shop.buy_rabbit()
                            print('----------------------------------КРОЛЕРЫНОК-------------------------------------')
                            print(rabbit)
                            price = random.randrange(10, 25)
                            print(f'Цена: {price} денюжек.')
                            line()
                            print(f'У вас в наличии {master.show_money()} денюжек.')

                            buy_command = input('''
1 - Покупаем этого кролика
2 - Покажи другого
0 - Уйти\nВыбор: ''')
                            match buy_command:
                                case '0':
                                    break
                                case '1':
                                    if master.show_money() >= price:
                                        line()
                                        cell.add_rabit(rabbit)
                                        master.withdraw_money(price)
                                        break
                                    else:
                                        print('Не хватает денюжек 😰')

                                case '2':
                                    pass


                    case '2': # Продать кролика
                        if len(cell.rabbits) == 0:
                            line()
                            print('У тебя нет кроликов. Кого ты продавать собрался?')
                            continue
                        if not (Rabbit in [type(rabbit) for rabbit in cell.rabbits]):
                            line()
                            print('Все твои кролики дохлые. Кого ты собрался переименовывать?')
                            continue

                        while True:
                            print('----------------------------------КРОЛЕРЫНОК-------------------------------------')
                            counter = 1
                            rabbits = []
                            for rabbit in cell.rabbits:
                                if type(rabbit) is not Dead_rabbit:
                                    rabbits.append(rabbit)
                            for rabbit in rabbits:
                                print(f'{counter}) {rabbit}')
                                print(f'        Цена: {int(shop.sell_rabbit(rabbit.lvl))}.\n')
                                counter += 1
                            line()
                            choice = input('''Кого хочешь продать?
Чтобы вернуться назад введите "0". 
Укажи порядковый номер: ''')
                            if choice == '0':
                                break
                            try:
                                choice = int(choice)
                                if choice > len(rabbits) or choice <= 0:
                                    line()
                                    print('Укажи порядковый номер кролика!')
                                    continue
                                else:
                                    rabbit = rabbits[choice - 1]
                                    price = int(shop.sell_rabbit(rabbit.lvl))
                                    line()
                                    print(f'{rabbit.name} продан(а) 😭. Будешь скучать?')
                                    print(f'Денюжки +{price}.')
                                    cell.rabbits.remove(rabbit)
                                    master.money += price

                                    break
                            except:
                                line()
                                print('Укажи порядковый номер кролика!')



                    case '3': # Продать мяско
                        if master.meat == 0:
                            line()
                            print('У тебя отсутствует мяско. Продавать нечего...')
                            continue
                        while True:
                            print('----------------------------------МЯСНАЯ ЛАВКА------------------------------------')
                            print(f'У вас в наличии: {master.show_meat()} 🥩.')
                            meats = input('''Сколько хотите продать?
Чтобы вернуться назад введите "0".
Укажите количество: ''')
                            try:
                                meats = int(meats)
                                if meats < 0 or meats > master.show_meat():
                                    line()
                                    print('Следует указать количества мяса, которое хотите продать.')
                                    continue
                                if meats == 0:
                                    break
                                master.meat -= meats
                                master.money += shop.sell_meats(meats)
                                line()
                                print(f'Мяско -{meats},\nДенюжки +{shop.sell_meats(meats)}.')
                                break
                            except:
                                line()
                                print('Следует указать количества мяса, которое хотите продать.')
                                continue



                    case '4': # Продать шкурки
                        if master.skin == 0:
                            line()
                            print('У тебя совсем нет шкурок. Что ты собрался продавать?')
                            continue
                        while True:
                            print('----------------------------------ШКУРНЫЕ ДЕЛА------------------------------------')
                            print(f'У вас в наличии: {master.show_skin()} 🦪.')
                            skins = input('''Сколько хотите продать?
Чтобы вернуться назад введите "0".
Укажите количество: ''')
                            try:
                                skins = int(skins)
                                if skins < 0 or skins > master.show_skin():
                                    line()
                                    print('Следует указать количество шкурок, которое хотите продать.')
                                    continue
                                if skins == 0:
                                    break
                                master.skin -= skins
                                master.money += shop.sell_skins(skins)
                                line()
                                print(f'Шкурки -{skins},\nДенюжки +{shop.sell_skins(skins)}.')
                                break
                            except:
                                line()
                                print('Следует указать количество шкурок, которое хотите продать.')
                                continue






        case '3':
            print('------------------------------------ИНВЕНТАРЬ-----------------------------------')
            print(f'''Инвентарь: 
Денюжки: {master.show_money()} 💰
Шкурки: {master.show_skin()} 🦪
Мяско: {master.show_meat()} 🥩''')












        case '4':
            actions = ['Ты похавал крольчатины. Изверг.',
                       'Ты поспал. С кайфом. Тебе снилась большая ферма кроликов.',
                       'Ты посмотрел дискавери. Было интересное шоу про кроликов.',
                       'Ты забил кальян. В качестве табачка украл немного сена из клетки. Вкусно было?',
                       'Ты посмотрел тик-токи. Ком данцен? Ихь виль нихьт.',
                       'Ты почитал новости. Не впечатлило.',
                       'Ты что-то искал в гараже. Не нашел.']
            line()
            print(random.choice(actions))
            if len(cell.rabbits) > 0:
                if Rabbit in [type(rabbit) for rabbit in cell.rabbits]:
                    cell.feeder -= random.randint(1, len(cell.rabbits))
                if cell.feeder > 0:
                    for rabbit in cell.rabbits:
                        if type(rabbit) is not Dead_rabbit:
                            if rabbit.health < 100:
                                rabbit.health += random.randint(5, 10)
                                if rabbit.health > 100:
                                    rabbit.health = 100
                if cell.feeder <= 0:
                    cell.feeder = 0
                    for rabbit in cell.rabbits:
                        if type(rabbit) is not Dead_rabbit:
                            rabbit.health -= random.randint(5, 15)
                            if rabbit.health <= 0:
                                line()
                                print(f'{rabbit.name} сдох(ла). Ты не уследил.Тебя бы не кормить столько.')
                                name = rabbit.name
                                cell.rabbits.remove(rabbit)
                                cell.rabbits.append(Dead_rabbit(name))

                if Rabbit in [type(rabbit) for rabbit in cell.rabbits]:
                    cell.drinking_bowl -= random.randint(1, len(cell.rabbits))
                if cell.drinking_bowl > 0:
                    for rabbit in cell.rabbits:
                        if type(rabbit) is not Dead_rabbit:
                            if rabbit.health < 100:
                                rabbit.health += random.randint(5, 10)
                                if rabbit.health > 100:
                                    rabbit.health = 100
                if cell.drinking_bowl <= 0:
                    cell.drinking_bowl = 0
                    for rabbit in cell.rabbits:
                        if type(rabbit) is not Dead_rabbit:
                            rabbit.health -= random.randint(5, 15)
                            if rabbit.health <= 0:
                                line()
                                print(f'{rabbit.name} сдох(ла). Ты не уследил. Тебя бы не поить столько.')
                                name = rabbit.name
                                cell.rabbits.remove(rabbit)
                                cell.rabbits.append(Dead_rabbit(name))

            for rabbit in cell.rabbits:
                if type(rabbit) is not Dead_rabbit:
                    rabbit.exp += random.randint(1, 3)
                    if rabbit.exp >= rabbit.max_exp:
                        rabbit.lvl += 1
                        rabbit.exp = 0
                        rabbit.add_max_exp()
                        cell.exp += random.randint(cell.lvl, 3*cell.lvl)
                        if cell.exp >= cell.amount_exp:
                            cell.lvl_up()







