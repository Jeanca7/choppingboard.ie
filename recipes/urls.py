from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('create_recipe/', views.show_recipe_form, name="show_recipe_form"),
    path('edit_recipe/<int:id>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('', views.recipes_list, name="home"),
    path('recipe_detail/<int:id>/', views.recipe_detail, name="recipe_detail"),
    path('recipe_like/', views.recipe_like, name='like'),
    path('list/', views.recipe_list, name='list'),
    path('cook_recipes_list/', views.cook_recipes_list, name='cook_recipes_list'),
]