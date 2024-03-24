from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('<h2>Главная Коты Собаки</h2>')

# def cats(request):
#     return HttpResponse('<h2>Коты</h2>')
#
# def dogs(request):
#     return HttpResponse('<h2>Собаки</h2>')
#

def pet(request, pet_slug):
    if pet_slug in  ['cats', 'dogs']:
        return HttpResponse(f'<h2>{pet_slug}</h2>')
    return HttpResponse(f'<h2>ОШИБКА!!! Нет такой страницы...</h2>')

def categories(request, categ_id):
    return HttpResponse(f'<h2>Категории<p> id: { categ_id } </p></h2>')