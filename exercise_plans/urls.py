from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise, name='exercise'),
    path('exercise/<int:pk>/', views.exercise_plans_detail,
         name='exercise_plans_detail'),
]
