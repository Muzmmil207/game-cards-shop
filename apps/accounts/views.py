from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserEditForm


@login_required
def wishlist(request):
    return render(request, "account/user/wishlist.html")


@login_required
def wallet(request):
    return render(request, "account/user/wallet.html")


@login_required
def account_charge_checkout(request):
    return render(request, "account/user/account-charge-checkout.html")


@login_required
def account_orders(request):
    return render(request, "account/user/orders.html")


@login_required
def edit_account(request):
    form = UserEditForm(instance=request.user)

    if request.method == "POST":
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "account/user/edit-account.html", context)


@login_required
def delete_user(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return redirect("delete_confirmation")
