from django.urls import path, re_path
import online_cinema.views as online



urlpatterns = [
    path('', online.index),
    path('<slug:film_slug>/', online.films),
    path('<slug:film_slug>/fb_edit/<int:fb_id>/', online.fb_edit),
    path('<slug:film_slug>/fb_delete/<int:fb_id>/', online.fb_delete),
]