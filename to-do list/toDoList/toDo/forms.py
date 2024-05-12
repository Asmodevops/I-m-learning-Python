from django import forms

class AddTaskForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.Textarea(attrs={'class': 'task-name'}),
        error_messages={
            'min_length': 'Слишком короткое название задачи.',
            'max_length': 'Слишком длинное название задачи.',
            'required': 'Необходимо ввести название задачи.'
        }
        )
    text = forms.CharField(
        min_length=6,
        max_length=300,
        widget=forms.Textarea(attrs={'class': 'task-text'}),
        error_messages={
            'min_length': 'Слишком короткое описание задачи.',
            'max_length': 'Слишком длинное описание задачи.',
            'required': 'Необходимо ввести описание задачи.'
        }
    )

