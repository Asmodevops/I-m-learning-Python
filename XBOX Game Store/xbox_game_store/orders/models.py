from django.contrib.auth.models import User
from django.db import models

from store.models import Game


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
