# Generated by Django 2.1 on 2021-11-25 00:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 25, 0, 48, 28, 564303, tzinfo=utc)),
        ),
    ]
