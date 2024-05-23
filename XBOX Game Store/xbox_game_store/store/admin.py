from django.contrib import admin
from .models import Game, Genre, Feature

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'release_date', 'publisher')
    search_fields = ('title', 'publisher')
    list_filter = ('genres', 'features', 'release_date')
    filter_horizontal = ('genres', 'features')

admin.site.register(Game, GameAdmin)
admin.site.register(Genre)
admin.site.register(Feature)
