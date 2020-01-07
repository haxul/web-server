from rest_framework import serializers
from firstapp.models import PizzaShop, Pizza


class PizzaShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaShop
        fields = ("name", "description", "rating", "url", "id")


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ("name", "short_description", "photo", "price", "id")
