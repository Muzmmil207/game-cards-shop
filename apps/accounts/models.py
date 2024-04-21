from django.contrib.auth.models import User
from django.db import models

from apps.shop.models import Game


class Wallet(models.Model):
    user = models.OneToOneField(User, related_name="wallet", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "game")  # Enforce unique wishlist items per user-game combo

    def __str__(self):
        return f"{self.user.username}'s wishlist item - {self.game.name}"
