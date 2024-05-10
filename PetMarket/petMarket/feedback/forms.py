from django import forms
from .models import Feedback



# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']   # ЛИБО, ЧТОБЫ ВЗАИМСТВОВАТЬ ВСЕ СРАЗУ ---> '__all__'
        labels = {'text': 'Ваш отзыв:'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 55, 'rows': 5, 'class': 'form-input'}),
        }