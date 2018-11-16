# Generated by Django 2.1.1 on 2018-10-07 05:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0003_branch_branchpin'),
        ('branchmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branchmanager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchmanagername', models.CharField(default='', max_length=50)),
                ('branchmanagerhouse', models.CharField(default='', max_length=50)),
                ('branchmanagerplace', models.CharField(default='', max_length=50)),
                ('branchmanagercity', models.CharField(default='', max_length=50)),
                ('branchmanagerdistrict', models.CharField(default='', max_length=50)),
                ('branchmanagerstate', models.CharField(default='', max_length=50)),
                ('branchmanagerpin', models.BigIntegerField(default='')),
                ('branchmanagerdob', models.DateField(default=datetime.date.today)),
                ('branchmanagerage', models.BigIntegerField(default='')),
                ('branchmanagerdoj', models.DateField(default=datetime.date.today)),
                ('branchmanagercontact', models.BigIntegerField(default='')),
                ('branchmanageremail', models.CharField(default='', max_length=50)),
                ('branchmanagerusername', models.CharField(default='', max_length=50)),
                ('branchmanagerpassword', models.CharField(default='', max_length=50)),
                ('branchmanagerstatus', models.BigIntegerField(default='')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch')),
            ],
        ),
    ]