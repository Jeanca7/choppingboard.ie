from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created_date', 'cook', 'views', 'users_like']