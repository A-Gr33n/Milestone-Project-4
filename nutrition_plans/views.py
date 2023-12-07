from django.shortcuts import render, get_object_or_404
from .models import Meal

# Create your views here.


def all_meals(request):
    """ A view to show all meals, including sorting and search queries """

    meals = Meal.objects.all()

    context = {
        'meals': meals,
    }

    return render(request, 'meals/nutrition_plans.html', context)


def nutrition_plans_detail(request, meal_id):
    """ A view to show individual product details """

    meal = get_object_or_404(Meal, pk=meal_id)

    context = {
        'meal': meal,
    }

    return render(request, 'meals/nutrition_detail.html', context)
