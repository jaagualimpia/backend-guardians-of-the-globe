# Generated by Django 4.2.5 on 2023-11-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='netWorth',
            field=models.FloatField(default=0.0),
        ),
    ]