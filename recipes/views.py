from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from django.utils import timezone 
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def show_recipe_form(request):
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES)
        recipe=form.save(commit=False)
        recipe.cook=request.user
        recipe.created_date = timezone.now()
        recipe.save()
        return redirect(recipe_detail, recipe.id)
    else:
        form=RecipeForm()
        return render(request, "recipes/recipe_form.html", {'form': form})

@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    recipe.delete()
    return redirect("/")



def recipes_list(request):
    recipes = Recipe.objects.filter(created_date__lte = timezone.now())
    return render(request, "recipes/recipes_list.html", {"recipes": recipes})
    
    
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    recipe.views += 1
    recipe.save()
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})

#edit recipe
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.method=="POST":
        form = RecipeForm(request.POST, instance=recipe)
        form.save()
        return redirect("/")
    else:
        form=RecipeForm(instance=recipe) #populate with the recipe
        return render(request, "recipes/recipe_form.html", {'form': form})