# Generated by Django 2.1.1 on 2018-10-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchasedetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasedetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(default='', max_length=20)),
                ('itemquantity', models.CharField(default='', max_length=20)),
                ('itembasicrate', models.CharField(default='', max_length=20)),
                ('itemunittotal', models.CharField(default='', max_length=20)),
                ('purchaseinvoice', models.BigIntegerField()),
            ],
        ),
    ]
