from django.shortcuts import render, HttpResponse


# Create your views here.

def dashboard(request):
    context={
        "heading":f"Welcome staff",
    }
    return render(request, 'dashboard.html',context)

def allocate_project(request):
    context={
        "heading":f"Project Allocation Window",
    }
    return render(request, 'allocate_projects.html',context)

def allocate_guides(request):
    return HttpResponse("Allocate- guides here")

def allocate_groups(request):
    return HttpResponse("Allocate- groups here")

def projectsview(request):
    return HttpResponse("View projects here")

def guidesview(request):
    return HttpResponse("Guides view here")