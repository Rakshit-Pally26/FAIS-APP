# Generated by Django 2.2.5 on 2019-10-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faisApp', '0014_auto_20191030_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet_streamer',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet_streamer',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
