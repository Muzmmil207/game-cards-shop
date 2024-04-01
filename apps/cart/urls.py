from django.urls import path

from . import views

urlpatterns = [
    path("", views.shopping_cart, name="shopping-cart"),
    path("cart-add", views.cart_add, name="cart-add"),
    path("cart-delete", views.cart_delete, name="cart-delete"),
    path("cart-update", views.cart_update, name="cart-update"),
]
