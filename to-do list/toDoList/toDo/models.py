from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)
