from django.shortcuts import redirect

def redirect_root_view(request):
    return redirect('recipeinfo_recipe_list_urlpattern')