from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        label="姓氏",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        label="名字",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    first_name = forms.CharField(
        label="姓氏",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        label="名字",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="舊密碼",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 'type': 'password'})
    )

    new_password1 = forms.CharField(
        label="新密碼",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 'type': 'password'})
    )

    new_password2 = forms.CharField(
        label="新密碼確認",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 'type': 'password'})
    )

    class Meta:
        model = User
        fields = '__all__'
