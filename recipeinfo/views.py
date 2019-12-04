from django.shortcuts import render
from django.views import View

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
        return render(
            request,
            'recipeinfo/recipe_list.html',
            {'recipe_list': Recipe.objects.all()}
        )

class BeverageList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/beverage_list.html',
            {'beverage_list': Beverage.objects.all()}
        )