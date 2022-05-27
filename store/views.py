from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.http import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):

    return render(request, "pages/index.html")

# @login_required
def member_info(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)

        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "pages/member_info.html", {"form": form})
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }

        return render(request, "pages/member_info.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)

        if form.is_valid():
            form.save()
            messages.success(request, "註冊成功")

            return redirect("/")
        else:
            return render(request, "registration/register.html", {"form": form})
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }

        return render(request, "registration/register.html", context)
