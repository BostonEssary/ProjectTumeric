import datetime
from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField


class Title(models.Model):
    title_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.title_text

class Body(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    body_text = QuillField()

    def __str__(self):
        return self.body_text
    