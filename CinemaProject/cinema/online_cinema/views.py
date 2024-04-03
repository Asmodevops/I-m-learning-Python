from django.http import HttpResponse
from django.shortcuts import render



# all_films = {
#     'Мастер и Маргарита': 'master-and-margarite',
#     'Артур, ты король': 'arthur-king'
# }

def index(request):
    return render(request, 'menu.html')

def films(request, film_slug):
    if film_slug in ['arthur-king', 'master-and-margarite']:
        return render(request, f'{film_slug}.html')
