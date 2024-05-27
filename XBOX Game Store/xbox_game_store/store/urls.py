from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('search/', views.game_search, name='search'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('personal-data/', views.personal_data, name='personal-data'),
    path('catalog/game/<int:game_id>/', views.show_game, name='game'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)