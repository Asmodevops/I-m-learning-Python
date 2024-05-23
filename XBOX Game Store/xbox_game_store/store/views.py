from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>ЗДЕСЬ БУДЕТ ГЛАВНАЯ СТРАНИЦА приложения XBOX Game Store</h1>')

def catalog(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ КАТАЛОГ ИГР приложения XBOX Game Store</h1>')

def catalog_by_id(request, cat_id):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ КАРТОЧКА ИГРЫ приложения XBOX Game Store</h1><h2>Игра № {cat_id}</h2>')

def catalog_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>ИЛИ ЗДЕСЬ БУДЕТ КАРТОЧКА ИГРЫ приложения XBOX Game Store</h1><h2>Игра: {cat_slug}</h2>')

