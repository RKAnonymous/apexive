# Generated by Django 4.2.9 on 2024-02-02 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0002_aircraft_enggroup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PolitlogHeader',
            new_name='PilotlogHeader',
        ),
    ]
