from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Exercise(models.Model):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    intensity = models.CharField(max_length=20)
   

    def __str__(self):
        return self.name


class WorkoutDay(models.Model):
    day_name = models.CharField(max_length=20)
    exercises = models.CharField(max_length=20)

    def __str__(self):
        return self.day_name


class FitnessPlan(models.Model):
    goal = models.CharField(max_length=50)
    workout_days = models.CharField(max_length=50)

    def __str__(self):
        return self.goal
