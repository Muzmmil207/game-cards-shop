from django.contrib import admin

from .models import Order, OrderItem

# admin.site.register(OrderItem)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    can_delete = False
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        "user",
        "full_name",
        "email",
        "phone",
        "created",
        "total_paid",
        "order_key",
        "payment_screenshot",
        "order_number",
    )
    inlines = [OrderItemInline]
