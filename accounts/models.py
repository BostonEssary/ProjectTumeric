from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from ProjectTumeric import settings
# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to= "avatars/")


