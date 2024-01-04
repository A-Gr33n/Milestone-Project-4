from django.shortcuts import render, get_object_or_404
from .models import Workout

def WorkoutView(request):
    """ A view to see workouts """
    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workout/workout.html', context)


def workout_detail(request, pk):
    """ A view to show individual product details """

    workout = get_object_or_404(Workout, pk=pk)

    context = {
        'workout': workout,
    }

    return render(request, 'workout/workout_detail.html', context)




