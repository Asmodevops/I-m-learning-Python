from django.db import models

class Animal(models.Model): # == созданию табицы в sql
    name = models.CharField(max_length=30) # атрибут с типом TEXT
    age = models.IntegerField(default=1) # INTEGER

