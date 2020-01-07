from django.shortcuts import render
from . import forms


def form_page(request):
    form = forms.NameForm()
    return render(request, "validformapp/form_page.html", {})
