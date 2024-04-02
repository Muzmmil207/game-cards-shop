from django.urls import path

from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("<slug:category_slug>/", views.shop, name="category-shop"),
    path("game-details/<slug:game_slug>/", views.game_details, name="game-details"),
]
