from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    # if request.method == "POST":
    return HttpResponse("this is login")