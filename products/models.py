from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self)
        return self.name
    
    def get_frienldy_name(self):
        return self.friendly_name 

class ProductAttribute(models.Model):
    
     
    def __str__(self):
        return self.name
    