# Generated by Django 2.2 on 2020-05-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_booking_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateTimeField(default='2000-12-12'),
        ),
    ]
