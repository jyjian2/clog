from django.urls import path

from recipeinfo.views import (
    IngredientList,
    Recipe_IngredientList,
    RecipeList,
    RecipeDetail,
)




urlpatterns = [
    path('ingredients/',
         IngredientList.as_view(),
         name='recipeinfo_ingredient_list_urlpattern'),

    path('recipe_ingredients/',
         Recipe_IngredientList.as_view(),
         name='recipeinfo_recipe_ingredient_list_urlpattern'),

    path('recipes/',
         RecipeList.as_view(),
         name='recipeinfo_recipe_list_urlpattern'),

    path('recipes/<int:pk>/',
        RecipeDetail.as_view(),
         name='recipeinfo_recipe_detail_urlpattern')
]

