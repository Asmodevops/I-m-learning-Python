from django.db import models
from django.contrib.auth.models import User


class PaymentStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_payment_complete = models.BooleanField(default=False)