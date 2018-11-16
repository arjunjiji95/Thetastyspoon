# Generated by Django 2.0.7 on 2018-08-30 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0003_branch_branchpin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableno', models.CharField(default='', max_length=50)),
                ('seatno', models.CharField(default='', max_length=10)),
                ('tablerate', models.CharField(default='', max_length=50)),
                ('tablestatus', models.CharField(default='', max_length=50)),
                ('branchmanager_id', models.BigIntegerField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch')),
            ],
        ),
    ]
