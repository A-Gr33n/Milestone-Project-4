from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages 
from django.db.models import Q
from .models import Meal

# Create your views here.


def all_meals(request):
    """ A view to show all meals, including sorting and search queries """

    meals = Meal.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('meals'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            meals = meals.filter(queries)


    context = {
        'meals': meals,
        'search_term' : query, 
    }

    return render(request, 'meals/nutrition_plans.html', context)


def nutrition_plans_detail(request, meal_id):
    """ A view to show individual nutrition details """

    meal = get_object_or_404(Meal, pk=meal_id)

    context = {
        'meal': meal,
    }

    return render(request, 'meals/nutrition_detail.html', context)
