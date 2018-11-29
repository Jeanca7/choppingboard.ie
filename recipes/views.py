from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from .forms import RecipeForm

# Create your views here.

def show_recipe_form(request):
    
    last_recipe = Recipe.objects.last()
    recipe_file = last_recipe.recipe_file
    
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    if recipe_form.is_valid():
        form.save()
    
    context = {'recipe_file': recipe_file, 'recipe_form':recipe_form}
    return render(request, 'recipes/recipe_form.html', context)


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipes_list.html", {"recipes": recipes})
    
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})

