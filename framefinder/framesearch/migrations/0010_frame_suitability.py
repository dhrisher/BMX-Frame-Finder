# Generated by Django 3.1.2 on 2021-03-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framesearch', '0009_frame_discipline_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='suitability',
            field=models.FloatField(default=0),
        ),
    ]
