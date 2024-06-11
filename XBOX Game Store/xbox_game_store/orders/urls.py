from django.urls import path
from orders import views


app_name = 'orders'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase/<int:product_id>/', views.increase, name='increase'),
    path('decrease/<int:product_id>/', views.decrease, name='decrease'),
]