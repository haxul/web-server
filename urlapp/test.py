from django.contrib import admin
from django.urls import path
from urlapp import views

urlpatterns = [
    path("", views.home, name="test"),
]
