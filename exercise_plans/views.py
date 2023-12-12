from django.shortcuts import render

from .models import Exercise
# Create your views here.

def exercise(request):
    """ A view to see exercise_plans """
    exercise = Exercise.objects.all()

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercise/exercise_plans.html')
