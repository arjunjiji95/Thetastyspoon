# Generated by Django 2.1.1 on 2018-11-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderfood', '0004_auto_20181106_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderfood',
            name='orderfoodstatus',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderfood',
            name='orderfoodtotalamount',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderfood',
            name='orderitemname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
