# Generated by Django 2.2.6 on 2019-10-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='total_rooms',
        ),
        migrations.AddField(
            model_name='rooms',
            name='room_type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]