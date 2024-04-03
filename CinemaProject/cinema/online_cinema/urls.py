from django.urls import path, re_path
import online_cinema.views as online



urlpatterns = [
    path('', online.index),
    path('<slug:film_slug>/', online.films),
]