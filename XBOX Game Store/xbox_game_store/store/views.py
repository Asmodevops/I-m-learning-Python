from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render

from store.models import Game, CarouselItem, News, Genre, Feature
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
        'news': news,
        'current_page': 'homepage',
    }

    return render(request, 'store/index.html', context=data)


def catalog(request):
    games_list = Game.objects.all()

    # Фильтрация по цене
    price_filters = request.GET.getlist('price')
    if price_filters:
        price_query = Q()
        if 'low' in price_filters:
            price_query |= Q(price__lte=1000)
        if 'medium' in price_filters:
            price_query |= Q(price__gt=1000, price__lte=2000)
        if 'high' in price_filters:
            price_query |= Q(price__gt=2000, price__lte=3000)
        if 'higher' in price_filters:
            price_query |= Q(price__gt=3000, price__lte=4000)
        if 'highest' in price_filters:
            price_query |= Q(price__gt=4000)
        games_list = games_list.filter(price_query)

    # Фильтрация по жанру
    genre_filters = request.GET.getlist('genre')
    if genre_filters:
        games_list = games_list.filter(genres__id__in=genre_filters)

    # Фильтрация по техническим возможностям
    feature_filters = request.GET.getlist('feature')
    if feature_filters:
        games_list = games_list.filter(features__id__in=feature_filters).distinct()

    paginator = Paginator(games_list, 10)  # Пагинация: по 10 игр на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        games = [{'id': game.id, 'title': game.title, 'image': game.banner_image.url, 'price': game.price, 'description': game.description} for game in page_obj]
        data = {
            'games': games,
            'has_next': page_obj.has_next(),
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
        }
        return JsonResponse(data)

    data = {
        'genres': Genre.objects.all(),
        'features': Feature.objects.all(),
        'page_obj': page_obj,
        'current_page': 'catalog',
    }

    return render(request, 'store/catalog.html', context=data)



def guarantee(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДУТ ОПИСАНЫ ГАРАНТИИ приложения XBOX Game Store</h1>')
def feedback(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДУТ ОТЗЫВЫ к приложению XBOX Game Store</h1>')

def game_search(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ СТРАНИЦА ПОИСКА ИГР приложения XBOX Game Store</h1>')

def show_game(request, game_id):
    print(game_id)
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ КАРТОЧКА ИГРЫ приложения XBOX Game Store</h1><h2> ID игры: {game_id}</h2>')

