# Generated by Django 2.1.1 on 2018-10-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menudescription',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='menu',
            name='menupic',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
