# Generated by Django 2.1.1 on 2018-11-09 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20181109_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='billno',
            new_name='orderfoodbillno',
        ),
    ]
