from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import *
from .models import User

from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)



def register_page(request):
    if request.user.is_authenticated:
        return redirect("home/")
    
    
    if request.method == 'POST':
        usernameField = request.POST.get("username", None)
        emailField = request.POST.get("email", None)
        lastNameField = request.POST.get("last_name", None)
        passwordField = request.POST.get('password', None)
        user = User(
            email=emailField,
            username=usernameField,
            last_name=lastNameField
        )
        user.set_password(passwordField)
        user.save()
        return redirect("/home/")
    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home/")

    else:
        if request.method == "POST":
            login_username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            user = authenticate(request, username=login_username, password=password)

    
            print(login_username, password)
            if user is not None:
                login(request, user)
                return redirect("/home/")
            else:
                print("ishlamadi")
                
        return render(request, "login.html")
    
def home_view(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/register/")