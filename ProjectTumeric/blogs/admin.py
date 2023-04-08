from django.contrib import admin
from django.db import models

from .models import Title, Body

class BodyInline(admin.StackedInline):
    model = Body
    extra = 1

class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title_text"]}),
        ("Date Information",{"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [BodyInline]


admin.site.register(Title, TitleAdmin)
admin.site.register(Body)
