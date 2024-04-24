from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Task

def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = {
            'tasks': tasks
        }
        return render(request, 'index.html', data)

    if request.method == 'POST':
        task_name = request.POST.get('task-name')
        task_text = request.POST.get('task-text')
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
                'task': task
            }

            return render(request, 'task_edit.html', data)
        except Task.DoesNotExist:
            return render(request, 'pageNotFound404.html')


    if request.method == 'POST':
        task_name = request.POST.get('task-name')
        task_text = request.POST.get('task-text')
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