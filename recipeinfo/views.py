from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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


class CategoryList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 5
    model = Category
    permission_required = 'recipeinfo.view_category'


class CategoryDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.view_category'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        ingredient_list = category.ingredients.all()
        return render(
            request,
            'recipeinfo/category_detail.html',
            {'category': category, 'ingredient_list': ingredient_list}
        )


class CategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CategoryForm
    model = Category
    permission_required = 'recipeinfo.add_category'


class CategoryUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'recipeinfo/category_form_update.html'
    permission_required = 'recipeinfo.change_category'


class CategoryDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.delete_category'
    model = Category
    success_url = reverse_lazy('recipeinfo_category_list_urlpattern')


class IngredientList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 10
    model = Ingredient
    permission_required = 'recipeinfo.view_ingredient'


class IngredientDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.view_ingredient'

    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        recipe_ingredient_list = ingredient.recipe_ingredients.all()
        if ingredient.is_vegetarian == 0:
            is_vegetarian = 'NO'
        else:
            is_vegetarian = 'YES'

        return render(
            request,
            'recipeinfo/ingredient_detail.html',
            {'ingredient': ingredient, 'is_vegetarian': is_vegetarian, 'recipe_ingredient_list': recipe_ingredient_list}
        )


class IngredientCreate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = IngredientForm
    model = Ingredient
    permission_required = 'recipeinfo.add_ingredient'


class IngredientUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'recipeinfo/ingredient_form_update.html'
    permission_required = 'recipeinfo.change_ingredient'


class IngredientDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.delete_ingredient'
    model = Ingredient
    success_url = reverse_lazy('recipeinfo_ingredient_list_urlpattern')


class Recipe_TypeList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 5
    model = Recipe_Type
    permission_required = 'recipeinfo.view_recipe_type'



class Recipe_TypeDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.view_recipe_type'

    def get(self, request, pk):
        recipe_type = get_object_or_404(Recipe_Type, pk=pk)
        recipe_list = recipe_type.recipes.all()
        return render(
            request,
            'recipeinfo/recipe_type_detail.html',
            {'recipe_type': recipe_type, 'recipe_list': recipe_list}
        )


class Recipe_TypeCreate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = Recipe_TypeForm
    model = Recipe_Type
    permission_required = 'recipeinfo.add_recipe_type'


class Recipe_TypeUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = Recipe_TypeForm
    model = Recipe_Type
    template_name = 'recipeinfo/recipe_type_form_update.html'
    permission_required = 'recipeinfo.change_recipe_type'


class Recipe_TypeDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.delete_recipe_type'
    model = Recipe_Type
    success_url = reverse_lazy('recipeinfo_recipe_type_list_urlpattern')


class DessertList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 5
    model = Dessert
    permission_required = 'recipeinfo.view_dessert'



class DessertDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.view_dessert'

    def get(self, request, pk):
        dessert = get_object_or_404(Dessert, pk=pk)
        recipe_list = dessert.recipes.all()
        return render(
            request,
            'recipeinfo/dessert_detail.html',
            {'dessert': dessert, 'recipe_list': recipe_list}

        )


class DessertCreate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = DessertForm
    model = Dessert
    permission_required = 'recipeinfo.add_dessert'


class DessertUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = DessertForm
    model = Dessert
    template_name = 'recipeinfo/dessert_form_update.html'
    permission_required = 'recipeinfo.change_dessert'


class DessertDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.delete_dessert'
    model = Dessert
    success_url = reverse_lazy('recipeinfo_dessert_list_urlpattern')


class BeverageList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 5
    model = Beverage
    permission_required = 'recipeinfo.view_beverage'


class BeverageDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.view_beverage'

    def get(self, request, pk):
        beverage = get_object_or_404(Beverage, pk=pk)
        recipe_list = beverage.recipes.all()
        return render(
            request,
            'recipeinfo/beverage_detail.html',
            {'beverage': beverage, 'recipe_list': recipe_list}

        )


class BeverageCreate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = BeverageForm
    model = Beverage
    permission_required = 'recipeinfo.add_beverage'


class BeverageUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = BeverageForm
    model = Beverage
    template_name = 'recipeinfo/beverage_form_update.html'
    permission_required = 'recipeinfo.change_beverage'


class BeverageDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.delete_beverage'
    model = Beverage
    success_url = reverse_lazy('recipeinfo_beverage_list_urlpattern')


class RecipeList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 5
    model = Recipe
    permission_required = 'recipeinfo.view_recipe'


class RecipeDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.view_recipe'

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


class RecipeCreate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = RecipeForm
    model = Recipe
    permission_required = 'recipeinfo.add_recipe'


class RecipeUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipeinfo/recipe_form_update.html'
    permission_required = 'recipeinfo.change_recipe'


class RecipeDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'recipeinfo.delete_recipe'
    model = Recipe
    success_url = reverse_lazy('recipeinfo_recipe_list_urlpattern')
