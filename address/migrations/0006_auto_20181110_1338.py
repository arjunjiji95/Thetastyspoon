# Generated by Django 2.1.1 on 2018-11-10 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_address_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='orderfoodbillno',
            new_name='billno',
        ),
    ]
