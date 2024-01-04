from django.contrib import admin
from .models import Workout

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'duration',
                    'intensity',
                    'day_name',
                    'goal',
                    'workout_days',
                    'image_url',
                    'image')


admin.site.register(Workout, WorkoutAdmin)
