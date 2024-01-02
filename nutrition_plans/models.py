from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Meal(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,)
   
    


    def __str__(self):
        return self.name


class NutritionPlan(models.Model):
    goal = models.CharField(max_length=50)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.goal
        
    def __str__(self):  
        return self.name
