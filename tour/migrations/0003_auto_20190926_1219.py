# Generated by Django 2.2.5 on 2019-09-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_comfavs_userfavs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comfavs',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
