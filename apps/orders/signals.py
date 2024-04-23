from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order


@receiver(post_save, sender=Order)
def update_order_number(sender, instance: Order, created, **kwargs):
    if created:
        instance.order_number = (instance.id + 27) * 3
        instance.save()
