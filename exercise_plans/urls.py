from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise, name='exercise_plans'),
    
]
