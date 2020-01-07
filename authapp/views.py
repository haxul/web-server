from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "authapp/index.html", {})


@login_required(login_url="http://localhost:8000/authapp/login/")
def main_page(request):
    return render(request, "authapp/home.html", {})
