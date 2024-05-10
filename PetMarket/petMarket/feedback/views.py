from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from feedback.forms import *




def feedback(request):
    if request.method == 'POST':
        text_feedback = request.POST.get('text')
        if len(text_feedback) > 0:
            Feedback.objects.create(text=text_feedback)
            return HttpResponse(f"""
            <h2>Ваш отзыв успешно отправлен</h2>
            <a href=""><button>Вернуться на страницу с отзывами</button></a>
    """)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    elif request.method == 'GET':
        results = Feedback.objects.all()
        data = {
            'feedback': results,
            'add_feedback_form': AddFeedbackForm()
        }

        return render(request, 'feedback.html', data)


def editFeedback(request, feedback_id):
    fb = Feedback.objects.get(id=feedback_id)
    if request.method == 'GET':
        data = {
            "feedback": fb,
            'add_feedback_form': AddFeedbackForm()
        }

        return render(request, 'editFeedback.html', data)

    elif request.method == 'POST':
        text_feedback = request.POST.get('text')
        if len(text_feedback) > 0:
            fb.text = text_feedback
            fb.update = True
            fb.save()
            return HttpResponseRedirect('/./feedback/')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteFeedback(request, feedback_id):
    try:
        Feedback.objects.get(id=feedback_id).delete()
        return HttpResponseRedirect('/./feedback/')
    except Feedback.DoesNotExist:
        return HttpResponseNotFound('''
            <h2>Отзыв не найден.</h2>
            <a href="/./feedback/"><button>Вернуться на страницу с отзывами</button></a>
            ''')









