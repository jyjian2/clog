from django.urls import path

from recipeinfo.views import (
    IngredientList,
    IngredientDetail,
    RecipeDetail,
    CategoryList,
    CategoryDetail,
    Recipe_TypeList,
    Recipe_TypeDetail,
    BeverageList,
    BeverageDetail,
    RecipeList,
)




urlpatterns = [


    path('categories/',
         CategoryList.as_view(),
         name='recipeinfo_category_list_urlpattern'),

    path('categories/<int:pk>/',
        CategoryDetail.as_view(),
         name='recipeinfo_category_detail_urlpattern'),

    path('ingredients/',
         IngredientList.as_view(),
         name='recipeinfo_ingredient_list_urlpattern'),

    path('ingredients/<int:pk>/',
        IngredientDetail.as_view(),
         name='recipeinfo_ingredient_detail_urlpattern'),

    path('recipe_types/',
         Recipe_TypeList.as_view(),
         name='recipeinfo_recipe_type_list_urlpattern'),

    path('recipe_types/<int:pk>/',
        Recipe_TypeDetail.as_view(),
         name='recipeinfo_recipe_type_detail_urlpattern'),

    path('beverages/',
         BeverageList.as_view(),
         name='recipeinfo_beverage_list_urlpattern'),

    path('beverages/<int:pk>/',
        BeverageDetail.as_view(),
         name='recipeinfo_beverage_detail_urlpattern'),

    path('recipes/',
         RecipeList.as_view(),
         name='recipeinfo_recipe_list_urlpattern'),

    path('recipes/<int:pk>/',
        RecipeDetail.as_view(),
         name='recipeinfo_recipe_detail_urlpattern')
]

