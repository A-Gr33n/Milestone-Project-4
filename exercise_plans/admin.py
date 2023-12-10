from django.contrib import admin
from .models import Exercise


# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 
    'duration', 
    'intensity', 
    'day_name', 
    'goal',
    'workout_days',
    'image_url',
    'image')


admin.site.register(Exercise, ExerciseAdmin)
