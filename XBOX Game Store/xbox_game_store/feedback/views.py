import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from feedback.forms import FeedbackForm
from feedback.models import Feedback


def get_random_feedbacks(count: int):
    fb_count = Feedback.objects.count()
    if fb_count <= count:
        fb = Feedback.objects.all()
    else:
        fb_ids = set()
        while len(fb_ids) < count:
            random_id = random.randint(1, fb_count)
            if Feedback.objects.filter(id=random_id).exists():
                fb_ids.add(random_id)
        fb = Feedback.objects.filter(id__in=fb_ids)
    return fb



def feedbacks(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            fb_id = request.POST.get('fb_id')
            fb = get_object_or_404(Feedback, id=fb_id)
            if fb.user == request.user or request.user.is_staff:
                fb.delete()
                return redirect('/feedback/')

        else:
            form = FeedbackForm(request.POST)
            if form.is_valid():
                fb = form.save(commit=False)
                fb.user = request.user
                fb.save()
                return redirect('/feedback/')
    else:
        feedbacks = get_random_feedbacks(10)
        form = FeedbackForm()

    data = {
        'title': 'Отзывы',
        'form': form,
        'feedbacks': feedbacks,
        'current_page': 'feedback',
    }
    return render(request, 'feedback/feedback.html', data)