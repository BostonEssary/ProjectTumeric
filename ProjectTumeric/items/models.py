from django.db import models
from django_quill.fields import QuillField
# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class QuillPost(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    content = QuillField()