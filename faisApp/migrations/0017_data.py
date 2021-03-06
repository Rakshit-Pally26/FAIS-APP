# Generated by Django 3.0.5 on 2020-10-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faisApp', '0016_realtime_usgs_data_avg_ht'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('latitude', models.CharField(max_length=12)),
                ('longitude', models.CharField(max_length=13)),
                ('time_stamp', models.TimeField()),
                ('date', models.DateField()),
                ('additional_info', models.TextField()),
            ],
        ),
    ]
