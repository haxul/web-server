from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import UserForm, PizzaShopForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def home(request):
    return render(request, "authapp/index.html", {})


@login_required(login_url="http://localhost:8000/authapp/login/")
def main_page(request):
    return render(request, "authapp/home.html", {})


def sign_up(request):
    user_form = UserForm()
    pizza_form = PizzaShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        pizza_form = PizzaShopForm(request.POST, request.FILES)
        if user_form.is_valid() and pizza_form.is_valid():

            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizza_shop = pizza_form.save(commit=False)
            new_pizza_shop.user = new_user
            new_pizza_shop.save()
            user = authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]
            )
            login(request, user)
            return redirect(home)
    return render(request, "authapp/sign_up.html", {"user_form": user_form, "pizza_form": pizza_form})
