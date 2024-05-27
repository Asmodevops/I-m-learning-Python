from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Game, CarouselItem, News, Genre, Feature
import random

def get_random_games(count: int):
    game_count = Game.objects.count()
    if game_count <= count:
        games = Game.objects.all()
    else:
        game_ids = set()
        while len(game_ids) < count:
            random_id = random.randint(1, game_count)
            if Game.objects.filter(id=random_id).exists():
                game_ids.add(random_id)
        games = Game.objects.filter(id__in=game_ids)
    return games


def index(request):
    games = get_random_games(8)

    carousel = CarouselItem.objects.all()
    news = News.objects.order_by('-id')[:2]


    data = {
        'games': games,
        'carousel': carousel,
        'news': news,
        'title': 'Главная страница',
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

    paginator = Paginator(games_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        games = [{'id': game.id,
             'title': game.title,
             'image': game.banner_image.url,
             'price': game.price,
             'description': game.description} for game in page_obj]

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
        'title': 'Каталог',
        'current_page': 'catalog',
    }

    return render(request, 'store/catalog.html', context=data)



def about(request):
    data = {
        'title': 'Гарантии',
        'current_page': 'about',
    }
    return render(request, 'store/about.html', data)

def agreement(request):
    data = {
        'title': 'Пользовательское соглашение'
    }
    return render(request, 'store/agreement.html', data)

def privacy(request):
    data = {
        'title': 'Политика конфиденциальности'
    }
    return render(request, 'store/privacy.html', data)

def personal_data(request):
    data = {
        'title': 'Согласие на обработку персональных данных'
    }
    return render(request, 'store/personal-data.html', data)


def feedback(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДУТ ОТЗЫВЫ к приложению XBOX Game Store</h1>')

def game_search(request):
    return HttpResponse(f'<h1>ЗДЕСЬ БУДЕТ СТРАНИЦА ПОИСКА ИГР приложения XBOX Game Store</h1>')

def show_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    games = get_random_games(6)
    while game in games:
        games = get_random_games(6)

    context = {
        'game': game,
        'games': games,
        'current_page': 'catalog',
        'title': game.title
    }
    return render(request, 'store/game.html', context)

