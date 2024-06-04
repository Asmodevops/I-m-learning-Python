from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pytz import timezone as pytz_timezone

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        moscow_tz = pytz_timezone('Europe/Moscow')
        self.created_at = timezone.now().astimezone(moscow_tz)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Review by {self.user.username} on {self.created_at}'