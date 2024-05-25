from django.contrib import admin
from .models import Game, Genre, Feature, CarouselItem, News


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'release_date', 'publisher')
    search_fields = ('title', 'publisher')
    list_filter = ('genres', 'features', 'release_date')
    filter_horizontal = ('genres', 'features')

@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('caption', 'game1', 'game2', 'game3')
    search_fields = ('caption', 'game1__title', 'game2__title', 'game3__title')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Genre)
admin.site.register(Feature)