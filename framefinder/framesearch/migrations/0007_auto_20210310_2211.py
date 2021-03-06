# Generated by Django 3.1.2 on 2021-03-10 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framesearch', '0006_auto_20210310_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='chainstay',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='frame',
            name='chainstay_processed',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='frame',
            name='head_tube_angle',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='frame',
            name='head_tube_processed',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='frame',
            name='seat_tube_angle',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='frame',
            name='seat_tube_processed',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
