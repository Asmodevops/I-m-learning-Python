from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import News
from store.models import Game, CarouselItem, GamePass
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


class HomePage(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'games': get_random_games(8),
        'carousel': CarouselItem.objects.all(),
        'news': News.objects.order_by('-id')[:2],
        'gamepass': GamePass.objects.all(),
        'title': 'Главная страница',
        'current_page': 'homepage',
    }


class AboutPage(TemplateView):
    template_name = 'main/about.html'
    extra_context = {
        'title': 'Гарантии',
        'current_page': 'about',
    }


def agreement(request):
    data = {
        'title': 'Пользовательское соглашение'
    }
    return render(request, 'main/agreement.html', data)


def privacy(request):
    data = {
        'title': 'Политика конфиденциальности'
    }
    return render(request, 'main/privacy.html', data)


def personal_data(request):
    data = {
        'title': 'Согласие на обработку персональных данных'
    }
    return render(request, 'main/personal-data.html', data)


def error_404(request, exception):
    return render(request, 'main/404.html', status=404)