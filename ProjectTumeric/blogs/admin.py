from django.contrib import admin
from django.db import models
from .models import Title, QuillPost
from django.forms import TextInput, Textarea
from django import forms
from django_quill import fields


class QuillWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.setdefault('cols', 60)
        attrs.setdefault('rows',1)
        super(QuillWidget, self).__init__(*args, **kwargs)

class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title_text"]}),
        ("Date Information",{"fields": ["pub_date"],}),
    ]

class QuillPostAdmin(admin.ModelAdmin):
   pass

admin.site.register(Title, TitleAdmin)
admin.site.register(QuillPost)



