from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from store import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('search/', views.game_search, name='search'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('search/', views.game_search, name='search'),
    path('personal-data/', views.personal_data, name='personal-data'),
    path('catalog/game/<int:game_id>/', views.ShowGame.as_view(), name='game'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)