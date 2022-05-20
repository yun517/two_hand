from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label = "帳號",
        widget = forms.TextInput(attrs={"class": "form-control"})
    )

    password1 = forms.CharField(
        label = "密碼",
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )

    password2 = forms.CharField(
        label = "密碼確認",
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label = "帳號",
        widget = forms.TextInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        label = "密碼",
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "password")
