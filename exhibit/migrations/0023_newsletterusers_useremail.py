# Generated by Django 2.2.1 on 2019-05-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0022_newsletterusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterusers',
            name='useremail',
            field=models.EmailField(default='type@yourmail.here', max_length=254),
        ),
    ]
