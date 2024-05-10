from django.db import models

class Feedback(models.Model):
    text = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    update = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)

