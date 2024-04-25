from .models import Category


def game_categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}

    return context
