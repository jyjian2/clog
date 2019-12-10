from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [

    path('',
         RedirectView.as_view(
             pattern_name='recipeinfo_recipe_list_urlpattern',
             permanent= False
         )),

    path('admin/', admin.site.urls),

    path('', include('recipeinfo.urls'))
]