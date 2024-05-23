from django.urls import path
from store import views

urlpatterns = [
    path('', views.index),
    path('catalog/', views.catalog),
    path('catalog/<int:cat_id>/', views.catalog_by_id),
    path('catalog/<slug:cat_slug>/', views.catalog_by_slug),
]
