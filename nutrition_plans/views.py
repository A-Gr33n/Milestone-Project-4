from django.shortcuts import render
from .models import Meal

# Create your views here.


def all_meals(request):
    """ A view to show all meals, including sorting and search queries """

    meals = Meal.objects.all()

    context = {
        'meals': meals,
    }

    return render(request, 'meals/nutrition_plans.html', context)
