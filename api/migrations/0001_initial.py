# Generated by Django 4.2.5 on 2023-09-19 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_person', models.IntegerField()),
                ('is_villain', models.BooleanField()),
                ('ability', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('fortune_origin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Villain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weakness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_person', models.IntegerField()),
                ('is_villain', models.BooleanField()),
                ('weakness', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.villain')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=15)),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Relationships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('hero1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_hero', to='api.hero')),
                ('hero2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_hero', to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('winned', models.BooleanField()),
                ('description', models.CharField(max_length=50)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
                ('villain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.villain')),
            ],
        ),
    ]