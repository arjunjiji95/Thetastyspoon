# Generated by Django 2.1.1 on 2018-11-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20181109_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]