# Generated by Django 4.0.10 on 2023-04-10 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_quillpost_remove_body_body_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='quillpost',
            name='title',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blogs.title'),
            preserve_default=False,
        ),
    ]
