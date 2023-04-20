from django.contrib import admin
from django.db import models
from .models import Podcast
from django.forms import TextInput, Textarea
from django import forms
from django_quill import fields

# Register your models here.

class PodcastsAdmin(admin.ModelAdmin):
    pass

    

admin.site.register(Podcast, PodcastsAdmin)
