from django import forms

from recipeinfo.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['category_name'].strip()
