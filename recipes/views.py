from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from django.utils import timezone 
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

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
        return render(request, "recipe/recipe_form.html", {'form': form})

@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    recipe.delete()
    return redirect("/")


def recipes_list(request):
    recipes = Recipe.objects.filter(created_date__lte = timezone.now())
    return render(request, "recipe/recipes_list.html", {"recipes": recipes})
    
    
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    recipe.views += 1
    recipe.save()
    return render(request, "recipe/recipe_detail.html", {"recipe": recipe})

#edit recipe
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.method=="POST":
        form = RecipeForm(request.POST, instance=recipe)
        form.save()
        return redirect("/")
    else:
        form=RecipeForm(instance=recipe) #populate with the recipe
        return render(request, "recipe/recipe_form.html", {'form': form})
        
@ajax_required
@login_required
@require_POST
def recipe_like(request):
    recipe_id = request.POST.get('id')
    action = request.POST.get('action')
    if recipe_id and action:
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            if action == 'like':
                recipe.users_like.add(request.user)
            else:
                recipe.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})