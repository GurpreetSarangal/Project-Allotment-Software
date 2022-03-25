from email.utils import encode_rfc2231
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from staff.models import allocationTable
from collegeAdmin.models import *
import re


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
    all_projects = project.objects.all()
    for proj in all_projects:
        temp = {
            "title":proj.name ,
            "language":proj.language,
            "tech":proj.tech,
        }
        # print(temp)
        context["projects"].append(temp)
    
    if request.method == "POST":
        print(request.POST)
        allocation_entry = {
            "rollNo1" : request.POST["rollNo1"],
            "rollNo2" : request.POST["rollNo2"],
            "project_title" : request.POST["project_title"],
            "lang" : request.POST["lang"],
            "tech" : request.POST["tech"],
        }
        print(allocation_entry)
        response = validate_allocation_form(allocation_entry)
        print("response = ",response)
        if response == "OK":
            add_entry_in_allocationsTable(allocation_entry)
            messages.success(request, "this project has been allocated!!")
        else:
            messages.error(request, response)
        return render(request, 'allocate_project.html',context)
    else:
        return render(request, 'allocate_project.html',context)

def allocate_guides_groups(request):
    return HttpResponse("Allocate- guides and groups here")

def projectswise(request):
    context = {
        "css":"allocate_project.css",
        "js":"allocate_project.js",
        "entries":[],
    }    
    context["entries"] = get_allocation_data()
    return render(request, 'project_wise_view.html',context)

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

def add_entry_in_allocationsTable(form):
    stu_1 = student.objects.get(rollNo=form["rollNo1"])
    proj = project.objects.get(
        name=form["project_title"],
        language=form["lang"],
        tech=form["tech"],
    )

    if form["rollNo2"] != "":
        stu_2 = student.objects.get(rollNo=form["rollNo2"])
        new_allocation = allocationTable(
            student_1 = stu_1,
            student_2 = stu_2,
            project = proj,
        )
        new_allocation.save()
    else:
        new_allocation = allocationTable(
            student_1 = stu_1,
            project = proj,
        )
        new_allocation.save()

def validate_allocation_form(form):
    if calculate_length(form["rollNo1"]) == 11:
        if calculate_length(form["rollNo2"]) == 11:
            if form["rollNo1"] != form["rollNo2"]:
                try:
                    class_1 = (student.objects.get(rollNo=form["rollNo1"])).className
                    class_2 = (student.objects.get(rollNo=form["rollNo2"])).className
                    if class_1 == class_2:
                        pass
                    else:
                        return "Students from different Classes"
                except:
                    return "RollNo(s) not Registered!!"
            else:
                return "Both RollNo are same"
        elif calculate_length(form["rollNo2"]) == 0:
            try:
                class_1 = (student.objects.get(rollNo=form["rollNo1"])).className
                print(class_1)
            except:
                return "RollNo Not Registered!!"
        else:
            return "Invalid RollNo2"
    else : 
        return "Invalid RollNO1"
    # ? and doing this will not break the code because we are only showing those options which are already registered in the projects
    check_project = project.objects.get(
        name=form["project_title"],
    )
    if form["lang"] == check_project.language and form["tech"] == check_project.tech:
        if is_already_allocated(form):
            return "Project Already allocated"
        else:
            pass
    
    else:
        
        same_project_different_lang(form)
        
        
    return "OK"
          
def is_already_allocated(form):
    proj = project.objects.get(
        name=form["project_title"],
        language=form["lang"],
        tech=form["tech"],
    )
    
    try:
        if_exists = allocationTable.objects.get(
            
            project=proj,
        )
        return True
    except:
        return False

def same_project_different_lang(form):
    new_project = project(
        name=form["project_title"],
        language=form["lang"],
        tech=form["tech"],
    )
    new_project.save()
    
   

def calculate_length(num):
    digits = re.split(r"[0-9]{1}?", num)
    return len(digits)-1

def get_allocation_data():
    entries = []
    all_allocation_data = allocationTable.objects.order_by("project")
    for entry in all_allocation_data:
        temp = {
            "className": entry.student_1.className,
            "session": entry.student_1.session,
            "student_1" : {
                "rollNo": entry.student_1.rollNo,
                "name": entry.student_1.name,
                "fatherName": entry.student_1.fatherName,
                "email": entry.student_1.email,
                "mobile1": entry.student_1.mobile_1,
                "mobile2": entry.student_1.mobile_2,
            }
        }

        if entry.student_2:
            temp["student_2"] = {
                "rollNo": entry.student_2.rollNo,
                "name": entry.student_2.name,
                "fatherName": entry.student_2.fatherName,
                "email": entry.student_2.email,
                "mobile1": entry.student_2.mobile_1,
                "mobile2": entry.student_2.mobile_2,
            }
        else:
            temp["student_2"] = None
        
        if entry.guide:
            temp["guide"] = {
                "name": entry.guide.name
            }
        else:
            temp["guide"] = {
                "name":"Not Allocated yet"
            }
        temp["project"]={
            "name": entry.project.name,
            "lang": entry.project.language,
        }

        entries.append(temp)

    return entries

    