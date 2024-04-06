from django.urls import path

import my_app.views as my_app

urlpatterns = [
    path('', my_app.index),
    path('products/', my_app.product),
    # path('product/<int:product_id>/', my_app.product),
    path('artwork/', my_app.artworks),
    path('artwork/<slug:art_slug>/', my_app.artwork),
]

