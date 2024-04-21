from django.http import HttpResponse, HttpResponseRedirect
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
        if request.method == 'GET':
            feedbacks = Feedback.objects.filter(film_name=film_slug)
            data = {
                'feedback': feedbacks
            }

            return render(request, f'{film_slug}.html', data)

        if request.method == 'POST':
            text_feedback = request.POST.get('feedback')
            if len(text_feedback) > 0:
                Feedback.objects.create(text=text_feedback, film_name=film_slug)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def fb_edit(request, fb_id, film_slug):
    fb_data = Feedback.objects.get(id=fb_id)
    if request.method == 'GET':
        data = {
            'fb': fb_data
        }

        return render(request, 'fb_edit.html', data)

    if request.method == 'POST':
        fb_text = request.POST.get('feedback')
        fb = Feedback.objects.get(id=fb_id)
        fb.text = fb_text
        fb.update = True
        fb.save()
        return HttpResponseRedirect('../../')

def fb_delete(request, fb_id, film_slug):
    try:
        fb = Feedback.objects.get(id=fb_id)
        fb.delete()
        return HttpResponseRedirect('../../')
    except Feedback.DoesNotExist:
        return HttpResponse('''
        <h2>Запрашиваемый отзыв не найден.</h2>
        <a href="../../"><button>Вернуться</button></a>
        ''')
