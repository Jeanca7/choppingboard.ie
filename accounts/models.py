from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png", null=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
