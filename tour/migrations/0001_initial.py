# Generated by Django 2.2.5 on 2019-09-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plotsector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_name', models.CharField(max_length=100)),
                ('contrib', models.FloatField()),
            ],
        ),
    ]
