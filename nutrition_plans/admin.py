from django.contrib import admin
from.models import Meal, Category


# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

  


class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'friendly_name', 'name')

admin.site.register(Meal, MealAdmin)
admin.site.register(Category, CategoryAdmin)