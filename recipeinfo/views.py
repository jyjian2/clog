from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from .models import(
    Ingredient,
    Recipe_Ingredient,
    Recipe,
    Beverage,
)


class IngredientList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/ingredient_list.html',
            {'ingredient_list': Ingredient.objects.all()}
        )

class IngredientDetail(View):
    def get(self, request, pk):
        ingredient = get_object_or_404(
            Ingredient,
            pk=pk
        )
        recipe_list = ingredient.get_recipes()
        return render_to_response(
            'recipeinfo/ingredient_detail.html',
            {'ingredient': ingredient, 'recipe_list': recipe_list}
        )

class Recipe_IngredientList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/recipe_ingredient_list.html',
            {'recipe_ingredient_list': Recipe_Ingredient.objects.all()}
        )

class RecipeList(View):
    def get(self, request):
        recipe_list = Recipe.objects.all()
        return render(
            request,
            'recipeinfo/recipe_list.html',
            {'recipe_list': recipe_list}
        )

class RecipeDetail(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        # recipe_ingredients is a related name of Recipe_Ingredients defined in model.py
        recipe_ingredient_list = recipe.recipe_ingredients.all()
        return render(
            request,
            'recipeinfo/recipe_detail.html',
            {'recipe': recipe, 'recipe_ingredient_list': recipe_ingredient_list}
        )

class BeverageList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/beverage_list.html',
            {'beverage_list': Beverage.objects.all()}
        )