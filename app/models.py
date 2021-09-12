from django.db import models

class Pessoas(models.Model):
    Nome = models.CharField(max_length=150)
    Profissão = models.CharField(max_length=100)
    Idade = models.IntegerField()

# Create your models here.
