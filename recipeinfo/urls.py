from django.urls import path

from recipeinfo.views import (
    CategoryList,
    CategoryDetail,
    CategoryCreate,
    CategoryUpdate,
    IngredientList,
    IngredientDetail,
    IngredientCreate,
    IngredientUpdate,
    Recipe_TypeList,
    Recipe_TypeDetail,
    Recipe_TypeCreate,
    Recipe_TypeUpdate,
    BeverageList,
    BeverageDetail,
    BeverageCreate,
    BeverageUpdate,
    RecipeList,
    RecipeDetail,
    RecipeCreate,
    RecipeUpdate,
    )




urlpatterns = [


    path('categories/',
         CategoryList.as_view(),
         name='recipeinfo_category_list_urlpattern'),

    path('categories/<int:pk>/',
        CategoryDetail.as_view(),
         name='recipeinfo_category_detail_urlpattern'),

    path('categories/create/',
        CategoryCreate.as_view(),
        name='recipeinfo_category_create_urlpattern'),

    path('categories/<int:pk>/update/',
        CategoryUpdate.as_view(),
         name='recipeinfo_category_update_urlpattern'),

    path('ingredients/',
         IngredientList.as_view(),
         name='recipeinfo_ingredient_list_urlpattern'),

    path('ingredients/<int:pk>/',
        IngredientDetail.as_view(),
         name='recipeinfo_ingredient_detail_urlpattern'),

    path('ingredients/create/',
        IngredientCreate.as_view(),
        name='recipeinfo_ingredient_create_urlpattern'),

    path('ingredients/<int:pk>/update/',
         IngredientUpdate.as_view(),
         name='recipeinfo_ingredient_update_urlpattern'),

    path('recipe_types/',
         Recipe_TypeList.as_view(),
         name='recipeinfo_recipe_type_list_urlpattern'),

    path('recipe_types/<int:pk>/',
        Recipe_TypeDetail.as_view(),
         name='recipeinfo_recipe_type_detail_urlpattern'),

    path('recipe_types/create/',
        Recipe_TypeCreate.as_view(),
        name='recipeinfo_recipe_type_create_urlpattern'),

    path('recipe_types/<int:pk>/update/',
         Recipe_TypeUpdate.as_view(),
         name='recipeinfo_recipe_type_update_urlpattern'),

    path('beverages/',
         BeverageList.as_view(),
         name='recipeinfo_beverage_list_urlpattern'),

    path('beverages/<int:pk>/',
        BeverageDetail.as_view(),
         name='recipeinfo_beverage_detail_urlpattern'),

    path('beverages/create/',
        BeverageCreate.as_view(),
        name='recipeinfo_beverage_create_urlpattern'),

    path('beverages/<int:pk>/update/',
         BeverageUpdate.as_view(),
         name='recipeinfo_beverage_update_urlpattern'),

    path('recipes/',
         RecipeList.as_view(),
         name='recipeinfo_recipe_list_urlpattern'),

    path('recipes/<int:pk>/',
        RecipeDetail.as_view(),
         name='recipeinfo_recipe_detail_urlpattern'),


    path('recipes/create/',
         RecipeCreate.as_view(),
         name='recipeinfo_recipe_create_urlpattern'),

    path('recipes/<int:pk>/update/',
         RecipeUpdate.as_view(),
         name='recipeinfo_recipe_update_urlpattern'),
]

