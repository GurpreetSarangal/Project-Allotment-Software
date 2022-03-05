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

def allocate_guides_groups(request):
    return HttpResponse("Allocate- guides and groups here")

def projectswise(request):
    return HttpResponse("Project wise here")

def guideswise(request):
    return HttpResponse("Guides wise here")

def add_projects(request):
    return HttpResponse("Add new projects  here")