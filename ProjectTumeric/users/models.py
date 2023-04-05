from django.db import models

class UserName(models.Model):
    username = models.CharField(max_length=20)

class Password(models.Model):
    password = models.CharField()