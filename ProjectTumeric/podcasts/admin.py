from django.contrib import admin
from django.db import models
from .models import Title, Audio
from django.forms import TextInput, Textarea
from django import forms
from django_quill import fields

# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title_text"]}),
        ("Date Information",{"fields": ["pub_date"],}),
    ]

class AudioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Title, TitleAdmin)
admin.site.register(Audio)