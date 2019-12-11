from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from recipeinfo.forms import CategoryForm, IngredientForm, Recipe_TypeForm, BeverageForm, RecipeForm, DessertForm
from recipeinfo.utils import PageLinksMixin
from .models import (
    Ingredient,
    Recipe,
    Beverage,
    Category,
    Recipe_Type,
    Dessert,
)


class CategoryList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Category


class CategoryDetail(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        ingredient_list = category.ingredients.all()
        return render(
            request,
            'recipeinfo/category_detail.html',
            {'category': category, 'ingredient_list': ingredient_list}
        )


class CategoryCreate(CreateView):
    form_class = CategoryForm
    model = Category


class CategoryUpdate(UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'recipeinfo/category_form_update.html'


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('recipeinfo_category_list_urlpattern')


class IngredientList(PageLinksMixin, ListView):
    paginate_by = 10
    model = Ingredient


class IngredientDetail(View):
    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        if ingredient.is_vegetarian == 0:
            is_vegetarian = 'NO'
        else:
            is_vegetarian = 'YES'

        return render(
            request,
            'recipeinfo/ingredient_detail.html',
            {'ingredient': ingredient, 'is_vegetarian': is_vegetarian}
        )


class IngredientCreate(CreateView):
    form_class = IngredientForm
    model = Ingredient


class IngredientUpdate(UpdateView):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'recipeinfo/ingredient_form_update.html'


class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('recipeinfo_ingredient_list_urlpattern')


class Recipe_TypeList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Recipe_Type


class Recipe_TypeDetail(View):
    def get(self, request, pk):
        recipe_type = get_object_or_404(Recipe_Type, pk=pk)
        recipe_list = recipe_type.recipes.all()
        return render(
            request,
            'recipeinfo/recipe_type_detail.html',
            {'recipe_type': recipe_type, 'recipe_list': recipe_list}
        )


class Recipe_TypeCreate(CreateView):
    form_class = Recipe_Type
    model = Recipe_Type


class Recipe_TypeUpdate(UpdateView):
    form_class = Recipe_TypeForm
    model = Recipe_Type
    template_name = 'recipeinfo/recipe_type_form_update.html'


class Recipe_TypeDelete(DeleteView):
    model = Recipe_Type
    success_url = reverse_lazy('recipeinfo_recipe_type_list_urlpattern')


class DessertList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Dessert


class DessertDetail(View):
    def get(self, request, pk):
        dessert = get_object_or_404(Dessert, pk=pk)
        recipe_list = dessert.recipes.all()
        return render(
            request,
            'recipeinfo/dessert_detail.html',
            {'dessert': dessert, 'recipe_list': recipe_list}

        )


class DessertCreate(CreateView):
    form_class = DessertForm
    model = Dessert


class DessertUpdate(UpdateView):
    form_class = DessertForm
    model = Dessert
    template_name = 'recipeinfo/dessert_form_update.html'


class DessertDelete(DeleteView):
    model = Dessert
    success_url = reverse_lazy('recipeinfo_dessert_list_urlpattern')


class BeverageList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Beverage


class BeverageDetail(View):
    def get(self, request, pk):
        beverage = get_object_or_404(Beverage, pk=pk)
        recipe_list = beverage.recipes.all()
        return render(
            request,
            'recipeinfo/beverage_detail.html',
            {'beverage': beverage, 'recipe_list': recipe_list}

        )


class BeverageCreate(CreateView):
    form_class = BeverageForm
    model = Beverage


class BeverageUpdate(UpdateView):
    form_class = BeverageForm
    model = Beverage
    template_name = 'recipeinfo/beverage_form_update.html'


class BeverageDelete(DeleteView):
    model = Beverage
    success_url = reverse_lazy('recipeinfo_beverage_list_urlpattern')


class RecipeList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Recipe


class RecipeDetail(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        # recipe_ingredients is a related name of Recipe_Ingredients defined in model.py
        recipe_ingredient_list = recipe.recipe_ingredients.all()
        is_vegetarian = True
        for ri in recipe_ingredient_list:
            if ri.ingredient.is_vegetarian == False:
                is_vegetarian = False

        return render(
            request,
            'recipeinfo/recipe_detail.html',
            {'recipe': recipe, 'recipe_ingredient_list': recipe_ingredient_list, 'is_vegetarian': is_vegetarian}
        )


class RecipeCreate(CreateView):
    form_class = RecipeForm
    model = Recipe


class RecipeUpdate(UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipeinfo/recipe_form_update.html'


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipeinfo_recipe_list_urlpattern')
