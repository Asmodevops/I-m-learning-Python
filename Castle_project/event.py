# Класс EventGenerator:
# Генерирует случайные события, которые могут произойти с замком.
# Включает методы для создания различных событий (нападение крыс, нападение другого замка, нападение варваров с чумой)
# и определения их воздействия на замок.
from random import randint


class EventGenerator:
    def __init__(self, castle):
        self._castle = castle
        pass

    def generate_event(self):
        randm = randint(0, 100)
        good = False
        if randm >= 95: # Хороший исход
            good = True
        if good:
            randm = randint(0, 10)
            match randm:
                case 0:
                    print(f'Ваша команда строителей нашла забытый сундук с редкими материалами, увеличивая прочность замка!')
                    temp = randint(4, 8)
                    self._castle.add_health(temp)
                    print(f'Прочность замка: +{temp}')
                case 1:
                    print(f'Строители нашли скрытый резерв материалов, что позволило им ускорить темпы строительства и повысить прочность замка!')
                    temp = randint(1, 4)
                    self._castle.add_health(randint(1, 4))
                    print(f'Прочность замка: +{temp}')
                case 2:
                    print(f'Специалист по безопасности обнаружил потенциальную опасность на рабочем месте и предпринял меры для ее устранения, что повысило общую прочность замка!')
                    temp = randint(4, 8)
                    self._castle.add_health(randint(4, 6))
                    print(f'Прочность замка: +{temp}')
                case 3:
                    print(f'Ваша команда строителей нашла забытый сундук с материалами, увеличивая прочность замка!')
                    temp = randint(1, 3)
                    self._castle.add_health(temp)
                    print(f'Прочность замка: +{temp}')
                case 4:
                    print(f'Один из рабочих предложил эффективный метод экономии ресурсов, что улучшило прочность замка!')
                    temp = randint(1, 4)
                    self._castle.add_health(temp)
                    print(f'Прочность замка: +{temp}')
                case 5:
                    print(f'На стройплощадке был организован праздник, на котором работники могли отдохнуть и поднять моральный дух, что положительно сказалось на довольстве!')
                    temp = randint(5, 7)
                    self._castle.add_contentment(temp)
                    print(f'Довольство граждан: +{temp}')
                case 6:
                    print(f'Один из работников выдвинул инновационное предложение, сокращающее время строительства и повышающее довольство трудового коллектива!')
                    temp = randint(4, 5)
                    self._castle.add_contentment(temp)
                    print(f'Довольство граждан: +{temp}')
                case 7:
                    print(f'Завершение строительства новых парков, скверов и зеленых зон создало дополнительные возможности для активного отдыха и релаксации, что положительно сказалось на душевном состоянии народа.')
                    temp = randint(1, 4)
                    self._castle.add_contentment(temp)
                    print(f'Довольство граждан: +{temp}')
                case 8:
                    print(f'Во время инспекции выявлены дополнительные возможности для улучшения качества стройки, что повысило прочность и довольство населения.')
                    temp_1 = randint(5, 10)
                    temp_2 = randint(3, 6)
                    self._castle.add_contentment(temp_1)
                    self._castle.add_health(temp_2)
                    print(f'Прочность замка: +{temp_1}\nДовольство граждан: +{temp_2}')
                case 9:
                    print(f'Введение новых социальных программ, направленных на поддержку малообеспеченных семей и пенсионеров, вызвало признание и благодарность среди жителей!')
                    temp = randint(2, 6)
                    self._castle.add_contentment(temp)
                    print(f'Довольство граждан: +{temp}')
                case 10:
                    print(f'Хоть сегодня и хороший день, но ничего не произошло!')
        else:
            randm = randint(0, 10)
            match randm:
                case 0:
                    print(f'Один из строителей травмировался на рабочем месте, что вызвало задержку в работе и снижение довольства коллектива.')
                    temp_1 = randint(10, 20)
                    temp_2 = randint(15, 24)
                    self._castle.reduce_health(temp_1)
                    self._castle.reduce_contentment(temp_2)
                    print(f'Прочность замка: -{temp_1}\nДовольство граждан: -{temp_2}')
                case 1:
                    print(f'Неожиданное изменение погоды привело к затоплению стройплощадки и повреждению материалов, что уменьшило прочность постройки.')
                    temp = randint(10, 20)
                    self._castle.reduce_health(temp)
                    print(f'Прочность замка: -{temp}')
                case 2:
                    print(f'Один из ключевых поставщиков не смог выполнить заказ в срок, что вызвало задержку в строительстве и снизило довольство работников.')
                    temp = randint(8, 16)
                    self._castle.reduce_contentment(temp)
                    print(f'Довольство граждан: -{temp}')
                case 3:
                    print(f'Появление паразитов или грызунов в стенах здания, что вызывает повреждения материалов и снижает прочность конструкции.')
                    temp = randint(10, 20)
                    self._castle.reduce_health(temp)
                    print(f'Прочность замка: -{temp}')
                case 4:
                    print(f'Неудачное качество строительных материалов привело к деформации стен и потере прочности, что требует замены или усиления конструкции.')
                    temp = randint(5, 30)
                    self._castle.reduce_health(temp)
                    print(f'Прочность замка: -{temp}')
                case 5:
                    print(f'Отказ техники на стройке привел к задержке в выполнении работ и вызвал недовольство у населения!')
                    temp = randint(10, 20)
                    self._castle.reduce_contentment(temp)
                    print(f'Довольство граждан: -{temp}')
                case 6:
                    print(f'От работника ушла жена и он очень расстроился...')
                    temp = randint(5, 10)
                    self._castle.reduce_contentment(temp)
                    print(f'Довольство граждан: -{temp}')
                case 7:
                    print(f'Рост преступности и нарушений общественного порядка в районе проживания вызывает страх и неудовольство у жителей, что влияет на их общее чувство безопасности и удовлетворенности!')
                    temp = randint(13, 23)
                    self._castle.reduce_contentment(temp)
                    print(f'Довольство граждан: -{temp}')
                case 8:
                    print(f'Недостаточные инвестиции в развитие инфраструктуры, такие как дороги, общественный транспорт или коммуникации, приводят к неудобствам и задержкам в повседневной жизни жителей, что снижает их довольство!')
                    temp = randint(10, 20)
                    self._castle.reduce_contentment(temp)
                    print(f'Довольство граждан: -{temp}')
                case 9:
                    print(f'Неэффективное управление бюджетом и недостаточная прозрачность в расходовании государственных средств вызывают недовольство и доводят до снижения доверия к правительству!')
                    temp = randint(15, 21)
                    self._castle.reduce_contentment(temp)
                    print(f'Довольство граждан: -{temp}')
                case 10:
                    print(f'Хоть сегодня и плохой день, но ничего не произошло! :)')
                    pass
