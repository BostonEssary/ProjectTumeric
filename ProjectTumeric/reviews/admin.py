from django.contrib import admin
from django.db import models
from .models import Review
from django.forms import TextInput, Textarea
from django_quill.forms import QuillWidget
from django_quill.fields import QuillField
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
 
   pass

class QuillPostAdmin(admin.ModelAdmin):
   pass

admin.site.register(Review, ReviewAdmin)

