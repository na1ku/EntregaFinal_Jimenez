from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', login_usuarios, name="Login"),
    path('logout', auth_views.LogoutView.as_view(), name='Logout'),
]