from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe

# Create your views here.

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipes_list.html", {"recipes": recipes})
    
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})