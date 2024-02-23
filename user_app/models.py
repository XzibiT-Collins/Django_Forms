from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields we want to add
    profile_pic = models.ImageField(upload_to='profile_pics')
    profile_link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
