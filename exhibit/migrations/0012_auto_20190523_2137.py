# Generated by Django 2.2.1 on 2019-05-23 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0011_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo_tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
