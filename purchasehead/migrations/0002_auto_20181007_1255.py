# Generated by Django 2.1.1 on 2018-10-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasehead', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasedetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.CharField(default='', max_length=20)),
                ('itemname', models.CharField(default='', max_length=20)),
                ('itemquantity', models.CharField(default='', max_length=20)),
                ('itembasicrate', models.CharField(default='', max_length=20)),
                ('itemunittotal', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='purchasehead',
            name='branchmanager_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
