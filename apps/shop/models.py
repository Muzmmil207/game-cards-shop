from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class CardManager(models.Manager):
    def get_queryset(self):
        return super(CardManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=125, db_index=True)
    slug = models.SlugField(max_length=125, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="games/")  # Optional image field
    category = models.ForeignKey(
        Category, related_name="cards", on_delete=models.SET_NULL, null=True, blank=True
    )
    created_by = models.ForeignKey(
        User, related_name="card_creator", on_delete=models.CASCADE, null=True, blank=True
    )
    slug = models.SlugField(max_length=125)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = CardManager()

    class Meta:
        verbose_name_plural = "Games"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Discount(models.Model):
    # discount_type = models.CharField(
    #     max_length=20,
    #     choices=(
    #         ("PERCENTAGE", "Percentage"),
    #         ("AMOUNT", "Fixed Amount"),
    #     ),
    # )
    discount_value = models.DecimalField(max_digits=7, decimal_places=0)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.discount_value}"

    @property
    def is_active(self):
        now = timezone.now()
        return self.start_date <= now and (self.end_date is None or self.end_date >= now)


class Card(models.Model):
    name = models.CharField(max_length=255)
    card_code = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = CardManager()

    class Meta:
        verbose_name_plural = "Cards"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.game.name})"

    def get_discounted_price(self):
        if self.discount and self.discount.is_active():
            discount_amount = self.discount.discount_value
            return self.price - discount_amount
        else:
            return self.price  # No discount applied

    @property
    def stock(self):
        quantity = 0
        return quantity
