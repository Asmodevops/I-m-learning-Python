from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render


from .models import Animal
def create_animal():
    animal = Animal.objects.create(name='Animal3', age=8)
# def create_animal():
#     animal = Animal.objects.create(name='Animal2', age=8)

def index(request):
    #create_animal()
    return render(request, "index.html")

# def cats(request):
#     return HttpResponse("<h2>Коты</h2>")
#
# def dogs(request):
#     return HttpResponse("<h2>Собаки</h2>")
#
class Cat:
    def __init__(self):
        self.name = "Cat"
        self.age = 3

    # def __repr__(self):
    #     return f"name: {self.name}, age: {self.age}"
def pet(request, pet_slug):
    data = {
        "pet_name": pet_slug,
        "pet_text": "Это текст про страницу с животными",
        "pet_list": ["Кот", "Собака", "Птицы"],
        "pet_int": 34,
        "pet_dict": {"cat": "Кот", "dog": "Собака"},
        "pet_obj": Cat()
    }
    # будем делать обращение к БД " существует ли pet_slug ?"
    if pet_slug in ['cats', 'dogs']:
        return render(request, "pet_page.html", context=data) # context преобразует все к строке
    return render(request, "pageNotFound404.html", status=404)

def petGET(request):
    #       запрос.МЕТОД.получить_значение()

    user_data = request.GET.get('search_field')
    user_data2 = request.GET.get('smthfield')

    return HttpResponse(f"<h2>{user_data}</h2><div>{user_data2}</div>")



def categories(request, categorie_id):
    return HttpResponse(f"<h2>Категории</h2><p>id:{ categorie_id }</p>")

