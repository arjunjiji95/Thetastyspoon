# Generated by Django 2.1.1 on 2018-11-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderfood', '0007_auto_20181110_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfood',
            name='orderfoodbillno',
            field=models.CharField(default='100', max_length=20),
        ),
    ]
