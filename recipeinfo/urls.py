from django.urls import path

from recipeinfo.views import (
    IngredientList,
    Recipe_IngredientList,
    RecipeList,
)




urlpatterns = [
    path('ingredient/',
         IngredientList.as_view(),
         name='recipeinfo_ingredient_list_urlpattern'),

    path('recipe_ingredient/',
         Recipe_IngredientList.as_view(),
         name='recipeinfo_recipe_ingredient_list_urlpattern'),

    path('recipe/',
         RecipeList.as_view(),
         name='recipeinfo_recipe_list_urlpattern'),


]

