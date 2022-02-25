from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def adminDashboard(request):
    return render(request, "dashboard.html")

def staffview(request):
    return HttpResponse("this is staff")
    pass

def guidesview(request):
    return HttpResponse("this is guides")
    pass

def sessionsview(request):
    return HttpResponse("this is sessions")
    pass

def classview(request):
    return HttpResponse("this is class")
    pass