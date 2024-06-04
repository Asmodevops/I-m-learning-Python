from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                'class': 'form-input',
                'placeholder': 'Напишите ваш отзыв...'})
        }