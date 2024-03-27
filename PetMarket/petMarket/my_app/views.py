from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h2>My App</h2> <ul><li>product/</li> <li>artwork/</li> </ul>')

def page1(request):
    return HttpResponse('<h2>Page1</h2>')

def page2(request):
    return HttpResponse('<h2>Page2</h2>')

def product(request, product_id):
    return HttpResponse(f'<h2>Продукт №{product_id}</h2><h3><p> ОПИСАНИЕ ПРОДУКТА №{product_id} </p></h3>')

def artwork(request, art_slug):
    if art_slug == 'mona-lisa':
        return HttpResponse(f'<img src="https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcQsu7yYuRPXNK9eHHSFD2tUYO4stQDb1Ez8vjqGERfs9xqYLLnY_y6lQkPFZa-44cqn" alt="">')
    elif art_slug == 'starry-night':
        return HttpResponse(f'<img src="https://sanctuarymentalhealth.org/wp-content/uploads/2021/03/The-Starry-Night-1200x630-1.jpg" alt="">')
    else:
        return HttpResponse(f'<img src="https://hozyindachi.ru/wp-content/uploads/2021/04/oshibka-404.jpg" alt="">')