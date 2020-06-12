# Generated by Django 2.2 on 2020-05-03 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=5)),
                ('available', models.BooleanField(default=False)),
                ('room_img', models.ImageField(upload_to='room images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.RoomType')),
            ],
        ),
    ]
