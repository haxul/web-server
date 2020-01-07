from django.shortcuts import render
from . import forms


def form_page(request):
    form = forms.NameForm()
    if request.method == "POST":
        form = forms.NameForm(request.POST)
        if form.is_valid():
            print("form is successfully")
            print(f"name: {form.cleaned_data['name']}")
            print(f"email: {form.cleaned_data['email']}")
            print(f"text: {form.cleaned_data['text']}")
    return render(request, "validformapp/form_page.html", {"form": form})
