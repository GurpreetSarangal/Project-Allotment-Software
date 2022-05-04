from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

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