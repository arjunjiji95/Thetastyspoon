# Generated by Django 2.1.1 on 2018-11-19 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportdate', models.DateField(default=datetime.date.today)),
                ('tablecount', models.BigIntegerField()),
                ('tableamt', models.BigIntegerField()),
                ('foodcount', models.BigIntegerField()),
                ('foodamt', models.BigIntegerField()),
                ('pcount', models.BigIntegerField()),
                ('pamt', models.BigIntegerField()),
                ('branch_id', models.BigIntegerField()),
            ],
        ),
    ]
