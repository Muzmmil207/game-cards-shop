from django.shortcuts import render


def wishlist(request):
    return render(request, "customers/wishlist.html")
