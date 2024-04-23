from django.contrib.auth import get_user_model
from django.db import models

from apps.shop.models import Card

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_order")
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    total_paid = models.DecimalField(max_digits=8, decimal_places=0)
    order_key = models.CharField(max_length=200)
    is_closed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name="item_card",
    )
    price = models.DecimalField(max_digits=7, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.card.game.name} {(self.card.name)}"
