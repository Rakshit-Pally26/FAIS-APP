# Generated by Django 2.1.7 on 2019-06-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='organization',
            field=models.CharField(default='Volunteer', max_length=100),
        ),
    ]
