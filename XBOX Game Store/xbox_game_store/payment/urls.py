from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('gamepass/<int:object_id>/', views.gamepass_pay, name='gamepass'),
    path('cart_pay/<int:cart_id>/', views.cart_pay, name='cart_pay'),
    # path('webhook/', views.yookassa_webhook, name='yookassa_webhook'),
]
