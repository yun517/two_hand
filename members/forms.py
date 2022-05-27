from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'class': 'form-control'}))
#     birth = forms.DateField(widget=forms.DateInput(
#         attrs={'class': 'form-control'}))
#     first_name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check'}))
    groups = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}))
    user_permission = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check'}))
    is_active = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'form-check'}))
    date_joined = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'


# class EditProfileForm(UserChangeForm):
#     first_name = forms.CharField(
#         label="姓氏",
#         widget=forms.TextInput(attrs={"class": "form-control", 'type':'text'})
#     )

#     last_name = forms.CharField(
#         label="名字",
#         widget=forms.TextInput(attrs={"class": "form-control", 'type':'text'})
#     )

#     email = forms.EmailField(
#         label="電子郵件",
#         widget=forms.EmailInput(attrs={"class": "form-control", 'type':'email'})
#     )

#     class Meta:
#         model = User
#         fields = '__all__'


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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"class": "form-control", 'type':'password'})
    )

    new_password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"class": "form-control", 'type':'password'})
    )

    new_password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={"class": "form-control", 'type':'password'})
    )

    class Meta:
        model = User
        fields = '__all__'
