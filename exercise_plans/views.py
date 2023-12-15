from django.shortcuts import render, get_object_or_404
from .models import Exercise

# Create your views here.

def exercise(request):
    """ A view to see exercise_plans """
    exercises = Exercise.objects.all()

    context = {
        'exercises': exercises,
    }

    return render(request, 'exercise/exercise_plans.html', context)


def exercise_plans_detail(request, pk):
    """ A view to show individual product details """

    exercise = get_object_or_404(Exercise, pk=pk)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercise/exercise_plans_detail.html', context)
