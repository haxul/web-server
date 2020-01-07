from django.http import JsonResponse
from .models import PizzaShop, Pizza
from .serializer import PizzaShopSerializer, PizzaSerializer


def client_get_pizzashops(request):
    pizza_shops = PizzaShopSerializer(
        PizzaShop.objects.all().order_by("-id"),
        many=True,
        context={"request": request}
    ).data
    return JsonResponse({"pizza_shops": pizza_shops})


def get_pizzas(request, pizzashop_id):
    pizzas = PizzaSerializer(
        Pizza.objects.all().filter(pizza_shop_id=pizzashop_id).order_by("-id"),
        many=True,
        context={"request": request}
    ).data
    return JsonResponse({"pizzas" : pizzas})
