# Generated by Django 2.1.1 on 2018-11-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchmanager', '0002_branchmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchmanager',
            name='branchmanageremail',
            field=models.EmailField(max_length=254),
        ),
    ]
