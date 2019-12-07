from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from recipeinfo.forms import CategoryForm, IngredientForm, Recipe_TypeForm, BeverageForm, RecipeForm
from recipeinfo.utils import ObjectCreateMixin
from .models import(
    Ingredient,
    Recipe,
    Beverage,
    Category,
    Recipe_Type,
)

class CategoryList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/category_list.html',
            {'category_list': Category.objects.all()}
        )


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

class IngredientList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/ingredient_list.html',
            {'ingredient_list': Ingredient.objects.all()}
        )

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

class Recipe_TypeList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/recipe_type_list.html',
            {'recipe_type_list': Recipe_Type.objects.all()}
        )

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


class BeverageList(View):
    def get(self, request):
        return render(
            request,
            'recipeinfo/beverage_list.html',
            {'beverage_list': Beverage.objects.all()}
        )

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