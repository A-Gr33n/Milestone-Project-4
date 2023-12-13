from django.shortcuts import render, get_object_or_404
from .models import Exercise

# Create your views here.

def exercise(request):
    """ A view to see exercise_plans """
    exercise = Exercise.objects.all()

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercise/exercise_plans.html')


def exercise_plans_detail(request, exercise_id):
    """ A view to show individual product details """

    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercise/exercise_plans_detail.html', context)
