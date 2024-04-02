from django.contrib import admin

from .models import Card, Category, Discount, Game

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Discount)
admin.site.register(Card)
