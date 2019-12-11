from django import forms

from recipeinfo.models import Category, Ingredient, Recipe_Type, Beverage, Recipe, Dessert


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_category_name(self):
        return self.cleaned_data['category_name'].strip()


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

    def clean_ingredient_name(self):
        return self.cleaned_data['ingredient_name'].strip()

    # def clean_is_vegetarian(self):
    #     return self.cleaned_data['is_vegetarian'].bin()


class Recipe_TypeForm(forms.ModelForm):
    class Meta:
        model = Recipe_Type
        fields = '__all__'

    def clean_recipe_type_name(self):
        return self.cleaned_data['recipe_type_name'].strip()


class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = '__all__'

    def clean_dessert_name(self):
        return self.cleaned_data['dessert_name'].strip()


class BeverageForm(forms.ModelForm):
    class Meta:
        model = Beverage
        fields = '__all__'

    def clean_beverage_name(self):
        return self.cleaned_data['beverage_name'].strip()

    def clean_beverage_type(self):
        return self.cleaned_data['beverage_type'].strip()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def clean_recipe_name(self):
        return self.cleaned_data['recipe_name'].strip()
