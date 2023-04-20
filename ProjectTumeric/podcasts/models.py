from django.db import models
from django.utils import timezone
# Create your models here.

class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='audio_files/%m/%d/')
    description = models.TextField(max_length=600)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.title
