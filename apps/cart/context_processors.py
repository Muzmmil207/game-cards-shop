from apps.shop.models import Card

from .cart import Cart


def cart(request):
    cart = Cart(request)
    cards = Card.objects.filter(id__in=cart.cart.keys())
    return {"cart": cart, "cart_cards": cards}
