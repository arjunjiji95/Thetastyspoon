# Generated by Django 2.1.1 on 2018-11-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_branch_branchpin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branchemail',
            field=models.EmailField(max_length=254),
        ),
    ]