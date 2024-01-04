from django.db import models

# Create your models here.


class Workout(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    intensity = models.CharField(max_length=20, null=True, blank=True)
    day_name = models.CharField(max_length=20, null=True, blank=True)
    goal = models.CharField(max_length=50, null=True, blank=True)
    workout_days = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sets = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
