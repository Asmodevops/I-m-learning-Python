from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def randomproduct():
    return random.randint(0, 9999)


def index(request):
    a = {
        'number': randomproduct()
    }
    return render(request, 'main_menu.html', context=a)


def product(request, product_id):
    return render(request, 'products.html', {'product_id': product_id})


def artworks(request):
    return render(request, 'artwork.html')


def artwork(request, art_slug):
    if art_slug == 'mona-lisa':
        return render(request, 'mona-lisa.html')
    elif art_slug == 'starry-night':
        return render(request, 'starry-night.html')
    else:
        return render(request, 'page404.html')