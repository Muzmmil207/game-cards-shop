from .models import Wishlist


def account_context(request):
    context = {"wishlist_count": 0}
    if request.user.is_authenticated:
        context["wishlist_count"] = Wishlist.objects.filter(user=request.user).count()

    return context
