# Generated by Django 2.2.1 on 2019-05-26 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0027_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='liked_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
