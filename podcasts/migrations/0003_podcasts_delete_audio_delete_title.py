# Generated by Django 4.0.10 on 2023-04-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_audio_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcasts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('audio_file', models.FileField(upload_to='audio_files/%m/%d/')),
                ('description', models.TextField(max_length=600)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
