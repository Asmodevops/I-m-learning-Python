from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

# def cats(request):
#     return HttpResponse('<h2>Коты</h2>')
#
# def dogs(request):
#     return HttpResponse('<h2>Собаки</h2>')
#
class Cat:
    def __init__(self):
        self.name = 'Cat'
        self.age = 3
    def __repr__(self):
        return f'name: {self.name} age: {self.age}'
def pet(request, pet_slug):
    data = {
        'pet': pet_slug,
        'pet_text': 'Это просто тест с животными.',
        'pet_list': ["Кот", "Собака", "Воробей", "Лошадь"],
        'pet_int': 34,
        'pet_dict': {'cat': 'Кот', 'dog': 'Собака'},
        'pet_object': Cat()
    }
    if pet_slug in ['cats', 'dogs']:
        return render(request, 'slug.html', context=data)
    # return HttpResponse('<h2>ОШИБКА!!! Нет такой страницы...</h2>')
    return render(request, 'pageNotFound.html', status=404)
def categories(request, categ_id):
    return HttpResponse(f'<h2>Категории<p> id: { categ_id } </p></h2>')