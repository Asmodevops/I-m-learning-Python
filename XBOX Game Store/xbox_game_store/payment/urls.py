from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('gamepass/<int:object_id>/', views.gamepass_pay, name='gamepass'),
    path('cart_pay/<int:cart_id>/', views.cart_pay, name='cart_pay'),
    path('webhook/', views.webhook, name='webhook'),
    path('payment_complete/', views.payment_complete, name='payment_complete'),
]
