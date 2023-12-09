from django.db import models

# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    intensity = models.CharField(max_length=20)
   

    def __str__(self):
        return self.name


class WorkoutDay(models.Model):
    day_name = models.CharField(max_length=20)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.day_name


class FitnessPlan(models.Model):
    goal = models.CharField(max_length=50)
    workout_days = models.ManyToManyField(WorkoutDay)

    def __str__(self):
        return self.goal
