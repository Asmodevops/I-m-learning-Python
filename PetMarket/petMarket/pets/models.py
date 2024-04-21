from django.db import models


class Animal(models.Model): # == созданию табицы в sql
    name = models.CharField(max_length=30) # атрибут с типом TEXT
    age = models.IntegerField(default=1) # INTEGER

class Feedback(models.Model):
    text = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    update = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)

