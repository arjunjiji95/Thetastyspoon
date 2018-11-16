# Generated by Django 2.0.7 on 2018-08-04 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodtype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(default='', max_length=20)),
                ('menuprice', models.CharField(default='', max_length=20)),
                ('foodtype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtype.Foodtype')),
            ],
        ),
    ]
