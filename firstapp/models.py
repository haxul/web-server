from django.db import models


class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name="Pizza shop title")
    description = models.TextField(max_length=400, verbose_name="Description")
    rating = models.FloatField(default=0, verbose_name="Rating")
    url = models.URLField(max_length=500, verbose_name="Shop Link")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=30, verbose_name="Pizza name")
    short_description = models.CharField(max_length=500, verbose_name="Description")
    price = models.IntegerField(default=0, verbose_name="Price")
    pizza_shop = models.ForeignKey(PizzaShop, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
