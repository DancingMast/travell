# Generated by Django 2.2.5 on 2019-10-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20190926_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='userfavs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
            ],
        ),
    ]