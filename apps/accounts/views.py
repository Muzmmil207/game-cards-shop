from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from apps.shop.models import Game

from .forms import UserEditForm
from .models import Wishlist


@login_required
def wishlist(request: HttpRequest):
    wishlists = Wishlist.objects.filter(user=request.user)
    context = {"wishlists": wishlists}
    return render(request, "account/user/wishlist.html", context)


@login_required
def wallet(request: HttpRequest):
    return render(request, "account/user/wallet.html")


@login_required
def account_charge_checkout(request: HttpRequest):
    return render(request, "account/user/account-charge-checkout.html")


@login_required
def account_orders(request: HttpRequest):
    return render(request, "account/user/account-orders.html")


@login_required
def edit_account(request: HttpRequest):
    form = UserEditForm(instance=request.user)

    if request.method == "POST":
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "account/user/edit-account.html", context)


@login_required
def delete_user(request: HttpRequest):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return redirect("delete_confirmation")


@login_required
def manage_wishlist(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    user = request.user

    # Check if game already exists in wishlist (optional)
    if not Wishlist.objects.filter(user=user, game=game).exists():
        Wishlist.objects.create(user=user, game=game)

    # Get the referrer URL (previous page)
    referer = request.META.get("HTTP_REFERER")

    # Check if referrer is valid and return a success message otherwise
    if not referer:
        return redirect("game-details", game.slug)  # Redirect to product detail

    return redirect(referer)  # Redirect back to the previous page
