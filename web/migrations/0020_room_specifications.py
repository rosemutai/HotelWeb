# Generated by Django 2.2 on 2020-10-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20200604_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Specifications',
            field=models.CharField(default='', max_length=300),
        ),
    ]