from django.db import models

class Title(models.Model):
    title_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField("date published")

class Body(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    body_text = models.TextField()