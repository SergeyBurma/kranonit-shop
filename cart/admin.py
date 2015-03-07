from django.contrib import admin
from cart.models import Order, OrderPosition


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderPositionInline,
    ]
    readonly_fields = ['created_at', 'closed_at']


admin.site.register(Order, OrderAdmin)
