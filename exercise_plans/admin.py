from django.contrib import admin
from .models import Exercise, WorkoutDay, FitnessPlan


# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'intensity')


class WorkoutDayAdmin(admin.ModelAdmin):
    list_display = ('day_name', 'exercises')


class FitnessPlanAdmin(admin.ModelAdmin):
    list_display = ('goal', 'workout_days')

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WorkoutDay, WorkoutDayAdmin)
admin.site.register(FitnessPlan, FitnessPlanAdmin)
