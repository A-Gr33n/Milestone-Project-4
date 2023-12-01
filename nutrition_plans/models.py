from django.db import models

# Create your models here.


class nutrition_plans(models.Model):
  name = models.CharField(max_length=254)
  description = models.TextField()