from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=254, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    cusine_type = models.CharField(max_length=254, default='')
    diet_type = models.CharField(max_length=254, default='')
    ingredients = models.TextField()
    preparation = models.TextField()
    image = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='videos', null=True)
    cook = models.ForeignKey(User, related_name="cook", null=False, default=1, on_delete=models.SET_DEFAULT)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.recipe_name



