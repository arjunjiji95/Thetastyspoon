# Generated by Django 2.1.1 on 2018-11-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablebook', '0010_auto_20181118_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebook',
            name='tableno',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
