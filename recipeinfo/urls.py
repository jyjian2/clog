from django.urls import path

from recipeinfo.views import (
    IngredientList,
    RecipeDetail,
    CategoryList,
    CategoryDetail,
    Recipe_TypeList,
    BeverageList,
    RecipeList,
)




urlpatterns = [

    path('categories/',
         CategoryList.as_view(),
         name='recipeinfo_category_urlpattern'),

    path('categories/<int:pk>/',
        CategoryDetail.as_view(),
         name='recipeinfo_category_detail_urlpattern'),

    path('ingredients/',
         IngredientList.as_view(),
         name='recipeinfo_ingredient_list_urlpattern'),

    path('recipe_types/',
         Recipe_TypeList.as_view(),
         name='recipeinfo_recipe_type_list_urlpattern'),

    path('beverages/',
         BeverageList.as_view(),
         name='recipeinfo_beverage_list_urlpattern'),

    path('recipes/',
         RecipeList.as_view(),
         name='recipeinfo_recipe_list_urlpattern'),

    path('recipes/<int:pk>/',
        RecipeDetail.as_view(),
         name='recipeinfo_recipe_detail_urlpattern')
]

