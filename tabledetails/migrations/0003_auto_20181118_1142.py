# Generated by Django 2.1.1 on 2018-11-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabledetails', '0002_remove_table_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='seatno',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='table',
            name='tablerate',
            field=models.BigIntegerField(),
        ),
    ]