# Generated by Django 4.0.10 on 2023-05-01 19:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='Profile',
        ),
    ]
