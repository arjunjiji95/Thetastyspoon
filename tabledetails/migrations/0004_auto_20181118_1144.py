# Generated by Django 2.1.1 on 2018-11-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabledetails', '0003_auto_20181118_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='tableno',
            field=models.BigIntegerField(),
        ),
    ]
