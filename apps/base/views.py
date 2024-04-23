from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from apps.shop.models import Game

from .forms import ContactForm


def index(request: HttpRequest):
    games_cards = Game.objects.filter(category__slug="games-cards")
    games_charge = Game.objects.filter(category__slug="games-charge")
    gift_cards = Game.objects.filter(category__slug="gift-cards")
    account_charge = Game.objects.filter(category__slug="account-charge")

    context = {
        "games_cards": games_cards,
        "games_charge": games_charge,
        "gift_cards": gift_cards,
        "account_charge": account_charge,
    }
    return render(request, "shop/index.html", context)


def about_us(request):

    return render(request, "about-us.html")


def faq(request):

    return render(request, "faq.html")


def contact_us(request: HttpRequest):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact-us")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def custom_404(request, exception):

    return render(request, "404.html", {}, status=404)
