from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .forms import AddTaskForm

def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = {
            'tasks': tasks,
            'task_add_form': AddTaskForm()
        }
        return render(request, 'index.html', data)

    if request.method == 'POST':
        task_name = request.POST.get('name')
        task_text = request.POST.get('text')
        if len(task_text) == 0 or len(task_name) == 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        Task.objects.create(name=task_name, text=task_text)
        return HttpResponseRedirect('../../')

def task_delete(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect('../../')
    except Task.DoesNotExist:
        return render(request, 'pageNotFound404.html')

def task_edit(request, task_id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id=task_id)
            data = {
                'task': task,
                'task_add_form': AddTaskForm()
            }

            return render(request, 'task_edit.html', data)
        except Task.DoesNotExist:
            return render(request, 'pageNotFound404.html')


    if request.method == 'POST':
        task_name = request.POST.get('name')
        task_text = request.POST.get('text')
        if len(task_text) == 0 or len(task_name) == 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        task = Task.objects.get(id=task_id)
        task.name = task_name
        task.text = task_text
        task.save()
        return HttpResponseRedirect('../../')

def task_done(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.status = True
        task.save()
        return HttpResponseRedirect('../../')
    except Task.DoesNotExist:
        return render(request, 'pageNotFound404.html')