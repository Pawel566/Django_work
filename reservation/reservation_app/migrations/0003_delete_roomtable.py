# Generated by Django 5.0.1 on 2024-01-17 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0002_rename_mytable_roomtable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoomTable',
        ),
    ]
