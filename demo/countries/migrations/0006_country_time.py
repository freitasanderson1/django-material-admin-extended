# Generated by Django 2.2.2 on 2019-06-25 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_country_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 6, 25, 6, 58, 3, 677090)),
            preserve_default=False,
        ),
    ]
