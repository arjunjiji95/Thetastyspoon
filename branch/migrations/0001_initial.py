# Generated by Django 2.0.7 on 2018-08-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(default='', max_length=20)),
                ('branchplace', models.CharField(default='', max_length=20)),
                ('branchcity', models.CharField(default='', max_length=20)),
                ('branchdistrict', models.CharField(default='', max_length=20)),
                ('branchcontact', models.CharField(default='', max_length=10)),
                ('branchemail', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
