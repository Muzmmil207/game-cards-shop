from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm


def index(request: HttpRequest):
    return render(request, "shop/index.html")


def about_us(request):

    return render(request, "about-us.html")


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
