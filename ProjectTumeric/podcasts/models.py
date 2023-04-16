from django.db import models
from django.utils import timezone
# Create your models here.

class Title(models.Model):
    id = models.AutoField(primary_key=True)
    title_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField("date published")


class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    audio_file = models.FileField(upload_to='audio_files/%m/%d/')
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    description = models.TextField(max_length=600)
    
