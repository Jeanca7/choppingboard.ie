from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_name', 'slug', 'image', 'created_date']
    list_filter = ['created_date']
