"""choppingboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include  
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static 
from accounts.views import register, dashboard, edit 
from recipes.views import recipes_list, recipe_detail, show_recipe_form, edit_recipe, delete_recipe
from donation.views import submit_donation, donation_checkout 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', recipes_list, name="home"),
    path('media/<path:path>/',serve, {'document_root': settings.MEDIA_ROOT}),
    path('recipe/<int:id>/', recipe_detail, name="recipe_detail"),
    path('post_recipe/', show_recipe_form, name="show_recipe_form"),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit_profile/', edit, name='edit'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('cook/donation/', submit_donation, name='submit_donation'),
    path('cook/donation_checkout/', donation_checkout, name='donation_checkout'),
    path('cook/edit_recipe/<int:id>/', edit_recipe, name='edit_recipe'),
    path('cook/delete_recipe/<int:id>/', delete_recipe, name='delete_recipe'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    