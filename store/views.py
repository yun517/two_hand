from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.http import *
from .forms import *
from .models import Good
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    good_list=Good.objects.all()
    context={
        'good_list':good_list
    }
    return render(request, "pages/index.html",context)

# @login_required
def member_info(request):
    if request.method == "POST":
        form = GoodModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "儲存成功")

    form = GoodModelForm()

    context = {
        "form": form
    }

    return render(request, "pages/member_info.html", context)

# def cart(request):

#     return render(request, "pages/cart.html")

# def saved_list(request):

#     return render(request, "pages/saved_list.html",context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)

        if form.is_valid():
            form.save()
            messages.success(request, "註冊成功")

            return redirect("/")
        else:
            return render(request, "pages/register.html", {"form": form})
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }

        return render(request, "pages/register.html", context)
