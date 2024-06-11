from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from store import views


app_name = 'store'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('gamepass/', views.GamePassPage.as_view(), name='gamepass'),
    path('search/', views.game_search, name='search'),
    path('game/<int:game_id>/', views.ShowGame.as_view(), name='game'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)