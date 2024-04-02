from django.contrib import admin

from .models import Card, Category, Discount, Game

admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Card)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Game, form, change) -> None:
        if not obj.pk:
            obj.created_by = request.user
        obj.save()
