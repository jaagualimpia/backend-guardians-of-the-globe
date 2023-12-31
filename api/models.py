from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

class Villain(models.Model):
    name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=15)
    origin = models.CharField(max_length=100)

class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    netWorth = models.FloatField(default=0.0)
    gender = models.CharField(max_length=15)
    dateOfbirth = models.DateField()
    fortune_origin = models.CharField(max_length=30)

class Abilities(models.Model):
    id_person = models.IntegerField()
    is_villain = models.BooleanField()
    ability = models.CharField(max_length=50)

class Weakness(models.Model):
    id_person = models.IntegerField()
    is_villain = models.BooleanField()
    weakness = models.CharField(max_length=50)

class Sponsorship(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.FloatField()

class Battle(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
    date = models.DateField()
    winned = models.BooleanField()

class Relationships(models.Model):
    hero1 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='first_hero')
    hero2 = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='second_hero')
    kind = models.CharField(max_length=50)

class Schedule(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    day = models.CharField(max_length=15)
    time = models.TimeField()
    duration = models.IntegerField()
