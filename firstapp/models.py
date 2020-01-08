from django.db import models
from django.contrib.auth.models import User


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
    photo = models.ImageField("Photo", upload_to="firstapp/photos", default="", blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT, verbose_name="Pizza")
    name = models.CharField(max_length=30, verbose_name="Customer name")
    phone = models.CharField(max_length=15, verbose_name="Phone")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Client")
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.get_full_name()
