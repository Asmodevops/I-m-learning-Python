from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('task_delete/<int:task_id>/', views.task_delete),
    path('task_done/<int:task_id>/', views.task_done),
    path('task_edit/<int:task_id>/', views.task_edit),
]
