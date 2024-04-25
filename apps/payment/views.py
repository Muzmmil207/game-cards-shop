import json

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from apps.accounts.models import Wallet
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
    context = {}
    cart = Cart(request)
    user = request.user
    has_enough_balance = False
    if user.is_authenticated:
        wallet = Wallet.objects.get(user=user)
        has_enough_balance = wallet.balance >= cart.get_cart_total()
        wallet.balance -= cart.get_cart_total()
    context["has_enough_balance"] = has_enough_balance

    if request.method == "POST":
        user = request.user
        cart_total = cart.get_cart_total()

        if request.FILES.get("payment_screenshot"):
            order = Order.objects.create(
                user=user,
                full_name=request.POST["first_name"] + " " + request.POST["last_name"],
                email=request.POST["email"],
                phone=request.POST["phone"],
                total_paid=cart_total,
                order_key=request.POST["order_key"],
                payment_screenshot=request.FILES.get("payment_screenshot"),
            )
        elif not request.FILES.get("payment_screenshot") and has_enough_balance:
            wallet.balance -= cart_total
            if wallet.balance >= 0:
                order = Order.objects.create(
                    user=user,
                    full_name=request.POST["first_name"] + " " + request.POST["last_name"],
                    email=request.POST["email"],
                    phone=request.POST["phone"],
                    total_paid=cart_total,
                    payment_method="wallet",
                )
                wallet.save()
        else:
            return redirect("checkout")

        for item in cart:
            OrderItem.objects.create(
                order=order, card=item["card"], price=item["price"], quantity=item["qty"]
            )

        cart.clear()
        return redirect("checkout-processed", order.id)
    return render(request, "payment/checkout.html", context)


@login_required
def checkout_processed(request: HttpRequest, order_id):
    user = request.user
    order = get_object_or_404(Order, id=order_id, user=user)
    # order.order_number = (order.id + 27) * 3
    # order.save()
    context = {"order": order}
    if not order.is_closed:
        return render(request, "payment/checkout-processed.html", context)
    return render(request, "account/user/order-details.html", context)
