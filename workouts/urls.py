from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutView, name='workout'),
    path('workout/<int:pk>/', views.workout_detail,
         name='workout_detail'),

]