# Generated by Django 4.2.9 on 2024-02-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='EngGroup',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]