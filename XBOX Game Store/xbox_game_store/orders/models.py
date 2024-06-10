import pytz
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from store.models import Game, GamePass


class CartItem(models.Model):
    product = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now().astimezone(pytz.timezone('Europe/Moscow'))
        super().save(*args, **kwargs)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        if isinstance(self.content_object, Game):
            return self.content_object.price * self.quantity
        elif isinstance(self.content_object, GamePass):
            return self.content_object.price
        return 0