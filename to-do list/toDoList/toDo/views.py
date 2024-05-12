from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTaskForm

def index(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            try:
                Task.objects.create(**form.cleaned_data)
                return redirect('/')
            except:
                form.add_error(None, 'Ошибка добавления задачи')

    if request.method == 'GET':
        form = AddTaskForm()

    tasks = Task.objects.all()
    data = {
        'tasks': tasks,
        'task_add_form': form,
    }

    return render(request, 'index.html', data)




def task_delete(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')
    except Task.DoesNotExist:
        return render(request, 'pageNotFound404.html')




def task_edit(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return render(request, 'pageNotFound404.html')

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            try:
                task.name = request.POST.get('name')
                task.text = request.POST.get('text')
                task.save()
                return redirect('/')
            except:
                form.add_error(None, 'Ошибка добавления задачи')

    elif request.method == 'GET':
        form = AddTaskForm()
    data = {
        'task': task,
        'task_add_form': form
    }
    return render(request, 'task_edit.html', data)


def task_done(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.status = True
        task.save()
        return redirect('/')
    except Task.DoesNotExist:
        return render(request, 'pageNotFound404.html')