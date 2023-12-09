from django.urls import path
from views import views

urlpatterns = [
    path('exercise_plans/', views.exercise_plans, name='exercise_plans'),
   
]
