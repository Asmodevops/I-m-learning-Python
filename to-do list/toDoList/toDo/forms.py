from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'text']
        widgets = {
            'name': forms.Textarea(attrs={'class': 'task-name'}),
            'text': forms.Textarea(attrs={'class': 'task-text'}),
        }