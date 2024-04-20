from django.db import models

# Create your models here.
class Feedback(models.Model):
    text = models.CharField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    film_name = models.CharField(max_length=300, null=True)
