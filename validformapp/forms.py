from django import forms
from django.core import validators


def check_first_letter(word):
    if word[0] != "A": raise forms.ValidationError("fuckin A")


class NameForm(forms.Form):
    name = forms.CharField(validators=[check_first_letter])
    email = forms.EmailField()
    vmail = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(50)])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data["email"]
        vmail = cleaned_data["vmail"]
        if email != vmail: raise forms.ValidationError("Not correct email")
        return cleaned_data
