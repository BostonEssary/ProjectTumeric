# Generated by Django 4.0.10 on 2023-04-10 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_quillpost_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quillpost',
            name='title',
        ),
    ]
