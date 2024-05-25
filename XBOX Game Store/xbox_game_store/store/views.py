from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from store.models import Game, CarouselItem, News
import random

def index(request):
    game_count = Game.objects.count()
    if game_count <= 8:
        games = Game.objects.all()
    else:
        game_ids = set()
        while len(game_ids) < 8:
            random_id = random.randint(1, game_count)
            if Game.objects.filter(id=random_id).exists():
                game_ids.add(random_id)
        games = Game.objects.filter(id__in=game_ids)

    carousel = CarouselItem.objects.all()
    news = News.objects.order_by('-id')[:2]


    data = {
        'games': games,
        'carousel': carousel,
        'news': news
    }

    return render(request, 'store/index.html', context=data)


def catalog(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ КАТАЛОГ ИГР приложения XBOX Game Store</h1>')

def guarantee(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДУТ ОПИСАНЫ ГАРАНТИИ приложения XBOX Game Store</h1>')
def feedback(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДУТ ОТЗЫВЫ к приложению XBOX Game Store</h1>')

def game_search(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ СТРАНИЦА ПОИСКА ИГР приложения XBOX Game Store</h1>')

def show_game(request, game_id):
    print(game_id)
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ КАРТОЧКА ИГРЫ приложения XBOX Game Store</h1><h2> ID игры: {game_id}</h2>')

