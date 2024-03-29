# Generated by Django 5.0.1 on 2024-01-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservation_app', '0003_delete_roomtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('projector_availability', models.BooleanField(default=False)),
            ],
        ),
    ]
