from django.http import HttpResponse
from django.shortcuts import render

from .models import Feedback


# all_films = {
#     'Мастер и Маргарита': 'master-and-margarite',
#     'Артур, ты король': 'arthur-king'
# }

def index(request):
    return render(request, 'menu.html')

def films(request, film_slug):
    if film_slug in ['arthur-king', 'master-and-margarite']:
        feedbacks = Feedback.objects.filter(film_name=film_slug)
        data = {
            'feedback': feedbacks
        }

        return render(request, f'{film_slug}.html', data)