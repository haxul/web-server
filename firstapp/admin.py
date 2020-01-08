from django.contrib import admin
from firstapp.models import PizzaShop, Pizza, Order, Client

admin.site.register(PizzaShop)
admin.site.register(Pizza)
admin.site.register(Client)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["pizza", "name", "phone", "date"]
