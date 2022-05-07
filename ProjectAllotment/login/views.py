from django import conf
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # TODO: add a landing page
    return redirect('login')

def login_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminDashboard')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            form = login(request, user)
            if request.user.is_superuser:
                return redirect('adminDashboard')
            return redirect('home')
        else:
            messages.error(request, "wrong credentials")
            return redirect('login')
    
    context = {
        "js" : "login_form.js",
        "css" : "login.css"
    }
    
    return render(request, 'login/login_form.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')

def reset_password(request):
    context = {
        "js" : "change_password.js",
        "css" : "change_password.css"
    }

    if(request.method == "POST"):
        username = request.user.username
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        user = authenticate(username=username, password=old_password)
        if user is None:
            messages.error(request, "wrong credentials")
        else:
            if new_password != confirm_password:
                messages.error(request, "New password did'nt match")
            else:
                user.set_password(new_password)
                user.save()
                messages.success(request, "New password is set")

    return render(request, "login/change_password.html", context)
    