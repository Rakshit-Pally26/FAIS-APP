# Generated by Django 2.1.7 on 2019-07-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faisApp', '0008_flood_station_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='select_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_code', models.CharField(max_length=2)),
                ('state_name', models.CharField(max_length=100)),
            ],
        ),
    ]
