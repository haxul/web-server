from django.shortcuts import render


def home(request, month, year):
    return render(request, "home.html", {"month": month, "year" : year})


def about(request):
    return render(request, "about.html", {})
