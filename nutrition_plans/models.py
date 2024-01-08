from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,)

    def __str__(self):
        return self.name

