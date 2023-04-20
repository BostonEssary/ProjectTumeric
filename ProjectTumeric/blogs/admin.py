from django.contrib import admin
from django.db import models
from .models import Blog
from django.forms import TextInput, Textarea
from django import forms
from django_quill import fields


class BlogAdmin(admin.ModelAdmin):
 
   pass


admin.site.register(Blog, BlogAdmin)


 

