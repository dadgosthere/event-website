# Generated by Django 5.0.2 on 2024-04-01 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=datetime.datetime(2024, 4, 1, 11, 57, 59, 899330, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
