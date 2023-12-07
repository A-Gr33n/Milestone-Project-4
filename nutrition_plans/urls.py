from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_meals, name='meals'),
    path('<meal_id>', views.nutrition_plans_detail, name='nutrition_detail')
]
