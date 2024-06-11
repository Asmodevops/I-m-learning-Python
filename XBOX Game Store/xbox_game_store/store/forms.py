from django import forms

class GameSearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)