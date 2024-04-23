from django import template

from apps.shop.models import Card

from ..cart import Cart

register = template.Library()


@register.filter
def get_quantity(card: Card, cart: Cart):
    try:
        return cart.cart.get(str(card.id))["qty"]
    except KeyError:
        return 1


@register.filter
def total_price(card: Card, cart: Cart):
    try:
        return int(cart.cart.get(str(card.id))["qty"]) * card.price
    except KeyError:
        return card.price


@register.filter
def order_item_total_price(order_item):
    return int(order_item.price) * order_item.quantity
