# Generated by Django 4.0.10 on 2023-04-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0003_podcasts_delete_audio_delete_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Podcasts',
            new_name='Podcast',
        ),
    ]
