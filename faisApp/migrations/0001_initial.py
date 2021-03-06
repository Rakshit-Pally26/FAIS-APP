# Generated by Django 2.1.7 on 2019-06-11 19:06

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='realtime_usgs_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.TextField()),
                ('id_num', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('flow', models.FloatField()),
                ('stage', models.FloatField()),
                ('url', models.URLField()),
            ],
            managers=[
                ('pdobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
