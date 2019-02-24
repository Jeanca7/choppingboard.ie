from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=254, default='')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    cusine_type = models.CharField(max_length=254, default='')
    diet_type = models.CharField(max_length=254, default='')
    ingredients = models.TextField()
    preparation = models.TextField()
    cook = models.ForeignKey(User, related_name='recipes_created', null=False, default=1, on_delete=models.SET_DEFAULT)
    views = models.IntegerField(default=0)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recipes_liked', blank=True)
    image = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='videos', null=False)
    
    def __str__(self):
        return self.recipe_name
        
    

    
    def get_absolute_url(self):
        return reverse('recipes:recipe_detail', args=[self.id])

