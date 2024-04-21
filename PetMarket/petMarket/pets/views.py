from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render


from .models import Animal, Feedback
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

def feedback(request):
    if request.method == 'POST':
        # ------------------- CREATE ---------------------#
        text_feedback = request.POST.get('feedback')
        if len(text_feedback) > 0:
            Feedback.objects.create(text=text_feedback)
            return HttpResponse(f"""
            <h2>Ваш отзыв успешно отправлен</h2>
            <a href=""><button>Вернуться на страницу с отзывами</button></a>
    """)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    elif request.method == 'GET':
        #------------------- READ ---------------------#
        #feedback получить все записи
        results = Feedback.objects.all()

        # передать в шаблон
        data ={
           "feedback": results
        }

        return render(request, 'feedback.html', data)

def editFeedback(request, feedback_id):
    feedbackData = Feedback.objects.get(id=feedback_id)
    if request.method == 'GET':
        #------------------- READ ---------------------#
        data = {
            "feedback": feedbackData
        }

        return render(request, 'editFeedback.html', data)

    elif request.method == 'POST':
        # ------------------- UPDATE ---------------------#
        text_feedback = request.POST.get('feedback')
        feedbackData.text = text_feedback
        feedbackData.update = True
        feedbackData.save()
        return HttpResponseRedirect('/pets/feedback/')

def deleteFeedback(request, feedback_id):
    try:
        Feedback.objects.get(id=feedback_id).delete()
        return HttpResponseRedirect('../../feedback/')
    except Feedback.DoesNotExist:
        return HttpResponseNotFound('''
        <h2>Отзыв не найден.</h2>
        <a href="../../feedback/"><button>Вернуться на страницу с отзывами</button></a>
        ''')