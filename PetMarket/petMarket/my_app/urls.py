from django.urls import path

import my_app.views as my_app

urlpatterns = [
    path('', my_app.index), # http://127.0.0.1:8000/my_app/
    path('page1/', my_app.page1), # http://127.0.0.1:8000/my_app/page1
    path('page2/', my_app.page2), # http://127.0.0.1:8000/my_app/page2
    path('product/<int:product_id>/', my_app.product),
    path('artwork/<slug:art_slug>/', my_app.artwork),
]

