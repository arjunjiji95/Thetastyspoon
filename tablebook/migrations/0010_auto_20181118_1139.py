# Generated by Django 2.1.1 on 2018-11-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablebook', '0009_auto_20181115_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebook',
            name='seatno',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablebook',
            name='tablerate',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
