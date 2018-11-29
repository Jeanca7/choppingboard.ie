from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=254, default='')
    cusine_type = models.CharField(max_length=254, default='')
    diet_type = models.CharField(max_length=254, default='')
    ingredients = models.TextField()
    preparation = models.TextField()
    image = models.ImageField(upload_to='images')
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    
    
    def __str__(self):
        return self.recipe_name +": " + str(self.videofile)
