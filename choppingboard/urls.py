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
from django.urls import path, include  #replace if necessary
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static 
from accounts.views import signup, show_profile 
from recipes.views import recipes_list, recipe_detail, show_recipe_form
from donation.views import submit_donation, donation_checkout 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipes_list, name="home"),
    path('media/<path:path>/',serve, {'document_root': settings.MEDIA_ROOT}),
    path('recipe/<int:id>/', recipe_detail, name="recipe_detail"),
    path('post_recipe/', show_recipe_form, name="show_recipe_form"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile/', show_profile, name='profile'),
    path('cook/donation/', submit_donation, name='submit_donation'),
    path('cook/donation_checkout/', donation_checkout, name='donation_checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
