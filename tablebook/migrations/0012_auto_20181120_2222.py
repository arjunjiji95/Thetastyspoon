# Generated by Django 2.1.1 on 2018-11-20 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablebook', '0011_tablebook_tableno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablebook',
            name='bookingrate',
        ),
        migrations.RemoveField(
            model_name='tablebook',
            name='bookingstatus',
        ),
    ]
