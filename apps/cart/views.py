import json

from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apps.shop.models import Card, Game

from .cart import Cart


def shopping_cart(request: HttpRequest):
    return render(request, "cart/shopping-cart.html")


@require_http_methods(["POST"])
def cart_add(request: HttpRequest):
    if request.method == "POST":
        cart = Cart(request)

        game_id = request.POST.get("game_id")
        game = get_object_or_404(Game, id=game_id)

        card_id = request.POST.get("card_id")
        card_qty = int(request.POST.get("quantity"))
        card = Card.objects.get(id=card_id)
        cart.add(card=card, qty=card_qty, card_game=game_id)

        return redirect("game-details", game.slug)  # Redirect to game detail
    return redirect("main-page")

    response = JsonResponse(f"{'product.title'} add to the cart", safe=False)
    return response


@csrf_exempt
@require_http_methods(["POST"])
def cart_update(request: HttpRequest):
    data = json.loads(request.body)
    cart = Cart(request)
    card_id = data.get("card_id")
    qty_value = int(data.get("qty_value"))
    cart.update(card_id=card_id, qty_value=qty_value)

    response = JsonResponse("cart updated", safe=False)
    return response


@require_http_methods(["POST"])
def cart_delete(request: HttpRequest):
    data = json.loads(request.body)
    cart = Cart(request)
    card_id = data.get("card_id")
    cart.delete(card_id=card_id)

    response = JsonResponse("cart updated", safe=False)
    return response


def cart_delete(request: HttpRequest, card_id):
    cart = Cart(request)
    cart.delete(card_id=card_id)

    # Get the referrer URL (previous page)
    referer = request.META.get("HTTP_REFERER")

    # Check if referrer is valid and return a success message otherwise
    if not referer:
        return redirect("shop")  # Redirect to product detail

    return redirect(referer)  # Redirect back to the previous page
