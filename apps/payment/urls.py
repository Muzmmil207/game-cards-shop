from django.urls import path

from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("checkout-processed/<str:order_id>/", views.checkout_processed, name="checkout-processed"),
    path("orderplaced/", views.order_placed, name="order_placed"),
    path("error/", views.Error.as_view(), name="error"),
]
