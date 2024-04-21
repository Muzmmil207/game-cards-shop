import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from apps.shop.models import Game

from .cart import Cart


def shopping_cart(request: HttpRequest):
    return render(request, "cart/shopping-cart.html")


@require_http_methods(["POST"])
def cart_add(request: HttpRequest):
    data = json.loads(request.body)
    print(data)
    # cart = Cart(request)
    # product_id = data.get("productid")
    # product_qty = int(data.get("productqty"))
    # product = Game.objects.get(id=product_id)
    # cart.add(product=product, qty=product_qty)

    response = JsonResponse(f"{'product.title'} add to the cart", safe=False)
    return response


@require_http_methods(["POST"])
def cart_update(request: HttpRequest):
    data = json.loads(request.body)
    cart = Cart(request)
    product_id = data.get("productid")
    action = data.get("action")
    cart.update(product_id=product_id, action=action)

    response = JsonResponse("cart updated", safe=False)
    return response


@require_http_methods(["POST"])
def cart_delete(request: HttpRequest):
    data = json.loads(request.body)
    cart = Cart(request)
    product_id = data.get("productid")
    cart.delete(product_id=product_id)

    response = JsonResponse("cart updated", safe=False)
    return response
