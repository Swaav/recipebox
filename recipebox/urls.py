"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
from .models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('recipe/<int:id>/', views.recipe_view),
    path('author/<int:id>/', views.author_view),
    path('recipeform/', views.recipe_form_view, name='recipeform'),
    path('authorform/', views.author_form_view, name='authorform'),
    path('favorite/<int:id>', views.recipe_favorite_view, name='favor'),
    path('edit/<int:id>', views.edit_recipe_view, name='editrecipe'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
