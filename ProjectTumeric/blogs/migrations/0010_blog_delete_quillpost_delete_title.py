# Generated by Django 4.0.10 on 2023-04-20 19:24

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_quillpost_id_alter_title_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('body', django_quill.fields.QuillField()),
                ('img_one', models.FileField(upload_to='review_img_1/%m/%d')),
                ('img_two', models.FileField(upload_to='review_img_2/%m/%d')),
                ('img_three', models.FileField(upload_to='review_img_3/%m/%d')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='QuillPost',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]