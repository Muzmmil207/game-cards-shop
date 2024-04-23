import json

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from apps.cart.cart import Cart
from apps.orders.models import Order, OrderItem
from apps.orders.views import payment_confirmation


def order_placed(request: HttpRequest):
    cart = Cart(request)
    cart.clear()
    return render(request, "payment/orderplaced.html")


class Error(TemplateView):
    template_name = "payment/error.html"


@login_required
def checkout(request: HttpRequest):

    cart = Cart(request)
    total = str(cart.get_cart_total())
    total = total.replace(".", "")
    total = int(total)

    stripe.api_key = settings.SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total, currency="usd", metadata={"userid": request.user.id}
    )

    return render(request, "payment/checkout.html", {"client_secret": intent.client_secret})


def checkout(request: HttpRequest):
    cart = Cart(request)

    if request.method == "POST":
        order_key = request.POST["order_key"]
        user = request.user
        cart_total = cart.get_cart_total()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user=user,
                full_name=request.POST["first_name"] + " " + request.POST["last_name"],
                email=request.POST["email"],
                phone=request.POST["phone"],
                total_paid=cart_total,
                order_key=order_key,
                payment_screenshot=request.FILES.get("payment_screenshot"),
            )

            for item in cart:
                OrderItem.objects.create(
                    order=order, card=item["card"], price=item["price"], quantity=item["qty"]
                )

            cart.clear()
            return redirect("checkout-processed", order.id)
    return render(request, "payment/checkout.html")


@login_required
def checkout_processed(request: HttpRequest, order_id):
    order = Order.objects.get(id=order_id)
    # order.order_number = (order.id + 27) * 3
    # order.save()
    context = {"order": order}
    return render(request, "payment/checkout-processed.html", context)
