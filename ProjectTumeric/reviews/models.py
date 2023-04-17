import datetime
from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = QuillField()
    img_one = models.FileField(upload_to='review_img_1/%m/%d')
    img_two = models.FileField(upload_to='review_img_2/%m/%d')
    img_three = models.FileField(upload_to='review_img_3/%m/%d')
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.title
    