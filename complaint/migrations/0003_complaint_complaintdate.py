# Generated by Django 2.1.1 on 2018-10-22 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_auto_20180827_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaintdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]