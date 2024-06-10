from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from store import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('catalog/', views.catalog, name='catalog'),
    path('gamepass/', views.GamePassPage.as_view(), name='gamepass'),
    path('search/', views.game_search, name='search'),
    path('personal-data/', views.personal_data, name='personal-data'),
    path('catalog/game/<int:game_id>/', views.ShowGame.as_view(), name='game'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
