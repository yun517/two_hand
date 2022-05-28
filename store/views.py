from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.http import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):

    return render(request, "pages/index.html")