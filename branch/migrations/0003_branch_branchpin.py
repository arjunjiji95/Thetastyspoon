# Generated by Django 2.0.7 on 2018-08-04 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_auto_20180804_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branchpin',
            field=models.CharField(default='', max_length=20),
        ),
    ]
