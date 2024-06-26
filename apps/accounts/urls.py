from django.urls import path

from . import views

urlpatterns = [
    path("edit-account/", views.edit_account, name="edit-account"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("manage-wishlist/<str:game_id>", views.manage_wishlist, name="manage-wishlist"),
    path("wallet/", views.wallet, name="wallet"),
    path("account-charge-checkout/", views.account_charge_checkout, name="account-charge-checkout"),
    path("orders/", views.account_orders, name="account-orders"),
]
