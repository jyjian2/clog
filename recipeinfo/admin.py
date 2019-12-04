from django.contrib import admin
from .models import Ingredient, Recipe, Recipe_Ingredient, Beverage, Category, Beverage_Ingredient, Recipe_Type

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient)
admin.site.register(Beverage_Ingredient)
admin.site.register(Category)
admin.site.register(Beverage)
admin.site.register(Recipe_Type)
# Register your models here.
