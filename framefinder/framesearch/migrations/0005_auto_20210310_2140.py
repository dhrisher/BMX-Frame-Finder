# Generated by Django 3.1.2 on 2021-03-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framesearch', '0004_auto_20210310_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='chainstay',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='frame',
            name='head_tube_angle',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='frame',
            name='seat_tube_angle',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
