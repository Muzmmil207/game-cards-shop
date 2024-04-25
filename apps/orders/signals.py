from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order, OrderItem


@receiver(post_save, sender=Order)
def update_order_number(sender, instance: Order, created, **kwargs):
    if created:
        instance.order_number = (instance.id + 27) * 3
        instance.save()
    else:
        if instance.is_closed:
            order_items = OrderItem.objects.filter(order=instance)
            for item in order_items:
                if item.card.card_code:
                    item.code = item.card.card_code
                    item.card.is_active = False
                    item.card.save()
                else:
                    item.code = "تم الشحن من داخل اللعبة"
                item.save()
