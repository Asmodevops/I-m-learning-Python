from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.



products = []
class Product:
    def __init__(self, name, description, price, quantity, image):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.image = image

product1 = Product('Pioneer CMA019 white',
                   'Рожковая кофеварка предназначена для приготовления кофе из молотых кофейных зерен, вспенивания молока для приготовления кофе «Капучино» и подогрева напитков горячим паром.',
                   12199,
                   37,
                   '0.jpg')
product2 = Product('Kitfort КТ-7121-3',
                   'Кофемашина капсульная Kitfort КТ-7121-3 представлена в ярком желтом корпусе. Прорезиненные ножки делают ее устойчивой на любой поверхности. Для приготовления напитка используются капсулы K-Cup или молотый кофе. В комплекте предусмотрена многоразовая капсула K-Cup, в которую засыпается молотый кофе. Можно использовать также и одноразовые. Прибор поддерживает давление 3.5 Бар, поэтому можно готовить латте, капучино, американо, лунго, эспрессо. Конструкцией Kitfort КТ-7121-3 предусмотрен резервуар для воды емкостью 0.36 л. Для защиты от попадания мелких частиц мусора используется многоразовый фильтр. Он вставляется в отверстие емкости. Кофеварка включается одной кнопкой. Функция подачи горячей воды дает возможность готовить чай.',
                   2899,
                   14,
                   '1.jpg')
product3 = Product('Pioneer CMA022 черный',
                   'Капсульная кофемашина с автоматическим капучинатором Pioneer CMA022 со съемным стеклянным контейнером для молока 900 мл, сенсорным управлением, итальянской помпой высокого давления 20 бар идеально подходит для автоматического приготовления в одно касание лунго и эспрессо, капучино и латте. Стильная, простая в использовании кофемашина сохранит Ваши утренние минуты и станет правильным выбором для дома или офиса.',
                   24199,
                   3,
                   '2.jpg')

product4 = Product('Pioneer CMA019 black черный',
                   'Рожковая кофеварка предназначена для приготовления кофе из молотых кофейных зерен, вспенивания молока для приготовления кофе «Капучино» и подогрева напитков горячим паром.',
                   12299,
                   0,
                   '3.jpg')

products.append(product1)
products.append(product2)
products.append(product3)
products.append(product4)


def randomproduct():
    return random.randint(0, 9999)


def index(request):
    return render(request, 'main_menu.html')


# def product(request, product_id):
#     return render(request, 'products.html', {'product_id': product_id})


def product(request):
    data = {'product_objects': products}
    return render(request, 'products.html', context=data)



def artworks(request):
    return render(request, 'artwork.html')


def artwork(request, art_slug):
    if art_slug == 'mona-lisa':
        return render(request, 'mona-lisa.html')
    elif art_slug == 'starry-night':
        return render(request, 'starry-night.html')
    else:
        return render(request, 'page404.html')