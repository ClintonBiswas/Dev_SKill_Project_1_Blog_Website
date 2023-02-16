from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_name')
    name = models.CharField(max_length=200, blank=True, verbose_name='Full Name')
    location = models.CharField(max_length=200, blank=True)
    bio= models.TextField(verbose_name='Tell me yourself', blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self) -> str:
        return self.name
