# Generated by Django 4.2.5 on 2023-11-11 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_genderr_sponsor_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='dateOfBirth',
            new_name='dateOfbirth',
        ),
    ]
