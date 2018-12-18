from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png", blank=True)
    
    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
