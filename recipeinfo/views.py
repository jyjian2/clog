from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from recipeinfo.forms import CategoryForm, IngredientForm, Recipe_TypeForm, BeverageForm, RecipeForm
from recipeinfo.utils import ObjectCreateMixin, PageLinksMixin
from .models import(
    Ingredient,
    Recipe,
    Beverage,
    Category,
    Recipe_Type,
)

class CategoryList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Category

# class CategoryList(View):
#     page_kwarg = 'page'
#     paginate_by = 6;
#     template_name = 'recipeinfo/category_list.html'
#
#     def get(self, request):
#         categories = Category.objects.all()
#         paginator = Paginator(
#             categories,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'category_list': page,
#         }
#         return render(
#             request, self.template_name, context)

class CategoryDetail(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        ingredient_list = category.ingredients.all()
        return render(
            request,
            'recipeinfo/category_detail.html',
            {'category': category, 'ingredient_list': ingredient_list}
        )

class CategoryCreate(ObjectCreateMixin, View):
    form_class = CategoryForm
    template_name = 'recipeinfo/category_form.html'

class CategoryUpdate(View):
    form_class = CategoryForm
    model = Category
    template_name = 'recipeinfo/category_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        category = self.get_object(pk)
        context = {'form': self.form_class(instance=category), 'category': category}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        category = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=category)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        else:
            context = {'form': bound_form, 'category': category}
            return render(request, self.template_name, context)


class CategoryDelete(View):
    def get(self, request, pk):
        category = self.get_object(pk)
        ingredients = category.ingredients.all()
        if ingredients.count() > 0:
            return render(request, 'recipeinfo/category_refuse_delete.html', {'category': category, 'ingredients': ingredients})
        else:
            return render(request, 'recipeinfo/category_confirm_delete.html', {'category': category})

    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)
    def post(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return redirect('recipeinfo_category_list_urlpattern')


class IngredientList(PageLinksMixin, ListView):
    paginate_by = 10
    model = Ingredient


# class IngredientList(View):
#     page_kwarg = 'page'
#     paginate_by = 10;
#     template_name = 'recipeinfo/ingredient_list.html'
#
#     def get(self, request):
#         ingredients = Ingredient.objects.all()
#         paginator = Paginator(
#             ingredients,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'ingredient_list': page,
#         }
#         return render(
#             request, self.template_name, context)

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

class IngredientCreate(ObjectCreateMixin, View):
    form_class = IngredientForm
    template_name = 'recipeinfo/ingredient_form.html'

class IngredientUpdate(View):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'recipeinfo/ingredient_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        ingredient = self.get_object(pk)
        context = {'form': self.form_class(instance=ingredient), 'ingredient': ingredient}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        ingredient = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=ingredient)
        if bound_form.is_valid():
            new_ingredient = bound_form.save()
            return redirect(new_ingredient)
        else:
            context = {'form': bound_form, 'ingredient': ingredient}
            return render(request, self.template_name, context)



class IngredientDelete(View):
    def get(self, request, pk):
        ingredient = self.get_object(pk)
        recipe_ingredients = ingredient.recipe_ingredients.all()
        beverage_ingredients = ingredient.beverage_ingredients.all()

        if recipe_ingredients.count() > 0 or beverage_ingredients.count() > 0:
            return render(request, 'recipeinfo/ingredient_refuse_delete.html', {'ingredient': ingredient, 'recipe_ingredients': recipe_ingredients, 'beverage_ingredients': beverage_ingredients})
        else:
            return render(request, 'recipeinfo/ingredient_confirm_delete.html', {'ingredient': ingredient})

    def get_object(self, pk):
        return get_object_or_404(Ingredient, pk=pk)
    def post(self, request, pk):
        ingredient = self.get_object(pk)
        ingredient.delete()
        return redirect('recipeinfo_ingredient_list_urlpattern')



class Recipe_TypeList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Recipe_Type


# class Recipe_TypeList(View):
#     page_kwarg = 'page'
#     paginate_by = 10;
#     template_name = 'recipeinfo/recipe_type_list.html'
#
#     def get(self, request):
#         recipe_types = Recipe_Type.objects.all()
#         paginator = Paginator(
#             recipe_types,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'recipe_type_list': page,
#         }
#         return render(
#             request, self.template_name, context)



class Recipe_TypeDetail(View):
    def get(self, request, pk):
        recipe_type = get_object_or_404(Recipe_Type, pk=pk)
        recipe_list = recipe_type.recipes.all()
        return render(
            request,
            'recipeinfo/recipe_type_detail.html',
            {'recipe_type': recipe_type, 'recipe_list': recipe_list}
        )


class Recipe_TypeCreate(ObjectCreateMixin, View):
    form_class = Recipe_TypeForm
    template_name = 'recipeinfo/recipe_type_form.html'


class Recipe_TypeUpdate(View):
    form_class = Recipe_TypeForm
    model = Recipe_Type
    template_name = 'recipeinfo/Recipe_Type_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        Recipe_Type = self.get_object(pk)
        context = {'form': self.form_class(instance=Recipe_Type), 'Recipe_Type': Recipe_Type}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        Recipe_Type = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=Recipe_Type)
        if bound_form.is_valid():
            new_Recipe_Type = bound_form.save()
            return redirect(new_Recipe_Type)
        else:
            context = {'form': bound_form, 'Recipe_Type': Recipe_Type}
            return render(request, self.template_name, context)


class Recipe_TypeDelete(View):
    def get(self, request, pk):
        recipe_type = self.get_object(pk)
        recipes = recipe_type.recipes.all()

        if recipes.count() > 0:
            return render(request, 'recipeinfo/recipe_type_refuse_delete.html', {'recipe_type': recipe_type, 'recipes': recipes})
        else:
            return render(request, 'recipeinfo/recipe_type_confirm_delete.html', {'recipe_type': recipe_type})

    def get_object(self, pk):
        return get_object_or_404(Recipe_Type, pk=pk)

    def post(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return redirect('recipeinfo_recipe_list_urlpattern')




class BeverageList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Beverage



# class BeverageList(View):
#     page_kwarg = 'page'
#     paginate_by = 10;
#     template_name = 'recipeinfo/beverage_list.html'
#
#     def get(self, request):
#         beverages = Beverage.objects.all()
#         paginator = Paginator(
#             beverages,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'beverage_list': page,
#         }
#         return render(
#             request, self.template_name, context)



class BeverageDetail(View):
    def get(self, request, pk):
        beverage = get_object_or_404(Beverage, pk=pk)
        recipe_list = beverage.recipes.all()
        return render(
            request,
            'recipeinfo/beverage_detail.html',
            {'beverage': beverage, 'recipe_list': recipe_list}

        )


class BeverageCreate(ObjectCreateMixin, View):
    form_class = BeverageForm
    template_name = 'recipeinfo/beverage_form.html'


class BeverageUpdate(View):
    form_class = BeverageForm
    model = Beverage
    template_name = 'recipeinfo/beverage_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        beverage = self.get_object(pk)
        context = {'form': self.form_class(instance=beverage), 'beverage': beverage}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        beverage = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=beverage)
        if bound_form.is_valid():
            new_beverage = bound_form.save()
            return redirect(new_beverage)
        else:
            context = {'form': bound_form, 'beverage': beverage}
            return render(request, self.template_name, context)


class BeverageDelete(View):
    def get(self, request, pk):
        beverage = self.get_object(pk)
        recipes = beverage.recipes.all()

        if recipes.count() > 0:
            return render(request, 'recipeinfo/beverage_refuse_delete.html', {'beverage': beverage, 'recipes': recipes})
        else:
            return render(request, 'recipeinfo/beverage_confirm_delete.html', {'beverage': beverage})

    def get_object(self, pk):
        return get_object_or_404(Beverage, pk=pk)

    def post(self, request, pk):
        beverage = self.get_object(pk)
        beverage.beverage_ingredients.all().delete()
        beverage.delete()
        return redirect('recipeinfo_beverage_list_urlpattern')



class RecipeList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Recipe


# class RecipeList(View):
#     page_kwarg = 'page'
#     paginate_by = 10;
#     template_name = 'recipeinfo/recipe_list.html'
#
#     def get(self, request):
#         recipes = Recipe.objects.all()
#         paginator = Paginator(
#             recipes,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw = self.page_kwarg,
#                 n = page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'recipe_list': page,
#         }
#         return render(
#             request, self.template_name, context)



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


class RecipeCreate(ObjectCreateMixin, View):
    form_class = RecipeForm
    template_name = 'recipeinfo/recipe_form.html'


class RecipeUpdate(View):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipeinfo/recipe_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        recipe = self.get_object(pk)
        context = {'form': self.form_class(instance=recipe), 'recipe': recipe}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        recipe = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=recipe)
        if bound_form.is_valid():
            new_recipe = bound_form.save()
            return redirect(new_recipe)
        else:
            context = {'form': bound_form, 'recipe': recipe}
            return render(request, self.template_name, context)

class RecipeDelete(View):
    def get(self, request, pk):
        recipe = self.get_object(pk)
        return render(request, 'recipeinfo/recipe_confirm_delete.html', {'recipe': recipe})

    def get_object(self, pk):
        return get_object_or_404(Recipe, pk=pk)

    def post(self, request, pk):
        recipe = self.get_object(pk)
        recipe.recipe_ingredients.all().delete()
        recipe.delete()
        return redirect('recipeinfo_recipe_list_urlpattern')