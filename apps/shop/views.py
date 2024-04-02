from django.core.paginator import Paginator
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Category, Game


def shop(request, category_slug=None):
    games = Game.objects.all()

    # Filter by category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        games = games.filter(category=category)

    query = request.GET.get("q")  # Get search query from URL parameter
    # Filter by keyword (case-insensitive search)
    if query:
        games = games.filter(name__icontains=query) | games.filter(description__icontains=query)

    category_query = request.GET.get("category")
    if category_query and category_query != "0":
        games = games.filter(category__slug=category_query)

    # Filter and sort based on query parameters in the URL
    sort_by = request.GET.get("sort_by")
    # Apply sorting based on selection
    if sort_by:
        if sort_by == "name_asc":
            games = games.order_by("name")
        elif sort_by == "name_desc":
            games = games.order_by("-name")
        elif sort_by == "price_low_to_high":
            games = games.order_by("price")
        elif sort_by == "price_high_to_low":
            games = games.order_by("-price")
        elif sort_by == "rating_high_to_low":
            games = games.order_by("-rating")  # Order by descending rating

    paginator = Paginator(games, 12)  # Adjust page size as needed
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    clean_paginate = "&".join(
        f"{key}={value}" for key, value in request.GET.items() if key != "page"
    )

    context = {
        "games": page_obj,
        "clean_paginate": clean_paginate,
        "current_category": category if category_slug else None,
        "sort_by": sort_by,
        "games_length": games.count(),
    }

    return render(request, "shop/shop.html", context)


def game_details(request: HttpRequest, game_slug):
    """Renders a game detail page with related reviews and images."""
    try:
        game = Game.objects.filter(slug=game_slug).first()
    except:
        return Http404()

    context = {
        "game": game,
    }
    return render(request, "shop/game-details.html", context)
