# Generated by Django 2.2 on 2020-05-04 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20200504_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
