from django.urls import path

from . import views

urlpatterns = [
    path("edit-account/", views.edit_account, name="edit-account"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wallet/", views.wallet, name="wallet"),
    path("account-charge-checkout/", views.account_charge_checkout, name="account-charge-checkout"),
]
