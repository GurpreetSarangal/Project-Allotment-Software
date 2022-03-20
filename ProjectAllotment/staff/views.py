from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from collegeAdmin.models import *

# Create your views here.

def dashboard(request):
    context = {
        "css":"staff_dashboard.css"
    }
    return render(request, 'staff_dashboard.html',context)

def allocate_project(request):
    context = {
        "css":"allocate_project.css",
        "js":"allocate_project.js",
        "projects":[],
    }
    if request.method == "POST":

        pass
    else:
        all_projects = project.objects.all()
        for proj in all_projects:
            temp = {
                "title":proj.name ,
                "language":proj.language,
                "tech":proj.tech,
            }
            # print(temp)
            context["projects"].append(temp)
        return render(request, 'allocate_project.html',context)

def allocate_guides_groups(request):
    return HttpResponse("Allocate- guides and groups here")

def projectswise(request):
    return HttpResponse("Project wise here")

def guideswise(request):
    return HttpResponse("Guides wise here")


def all_projects(request):
    context = {
        "css":"all_project.css",
        "projects": [
            
        ]
    }
    all_projects = project.objects.all()
    for pro in all_projects:
        proj_details = {
            "id": pro.id,
            "name":pro.name,
            "lang":pro.language,
            "tech":pro.tech,
        }
        context["projects"].append(proj_details)
    return render(request, "all_project.html",context)

def add_projects(request):
    context = {
        "css" : "add_project.css"
    }
    if request.method == "POST":
        project_name = request.POST['project_name']
        project_lang = request.POST['project_lang']
        project_tech = request.POST['project_tech']
        new_project = project(
            name=project_name,
            language=project_lang,
            tech=project_tech,
        )
        messages.info(request, 'New Project has been added successfully!')
        new_project.save()
    return render(request, "add_project.html",context)

def edit_projects(request,id):
    curr_proj = project.objects.get(id=id)
    if request.method == "POST":
        new_title = request.POST["project_name"]
        new_lang = request.POST["project_lang"]
        new_tech = request.POST["project_tech"]
        curr_proj.name = new_title
        curr_proj.language = new_lang
        curr_proj.tech = new_tech
        messages.info(request, 'Project discription has been changed successfully!')
        curr_proj.save()
        

    context={
        "css":"edit_project.css",
        "project":{
            "id":curr_proj.id,
            "name":curr_proj.name,
            "lang":curr_proj.language,
            "tech":curr_proj.tech,
        }
    }
    return render(request, "edit_project.html",context)

def delete_projects(request, id):
    project.objects.get(id=id).delete()
    return redirect( "all-project")