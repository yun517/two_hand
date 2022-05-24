from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),    
    path("member_info/", views.member_info),
]