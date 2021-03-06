# Generated by Django 3.1.2 on 2020-12-23 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingorder',
            name='no_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bookingorder',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 10, 48, 25, 92006)),
        ),
        migrations.AlterField(
            model_name='bookingorder',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 24, 10, 48, 25, 92006)),
        ),
    ]
