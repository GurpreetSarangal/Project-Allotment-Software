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

def allocate_project(request, className="all"):
    context = {
        "css":"allocate_project.css",
        "js":"allocate_project.js",
        "projects":[],
    }
    
    
    if className == "all":
        # render the select_class_page.html
        context["css"] = "select_class_page.css"
        context["classes"] = []
        classes = student.objects.all().values("className").distinct()
        for class_ in classes:
            context["classes"].append(class_["className"])

        # print(context["classes"])
        return render(request, 'select_class_page.html',context)
        
    elif request.method == "POST":
        print(request.POST)
        allocation_entry = {
            "className" : className,
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


    # all_projects = project.objects.all()

    all_projects_ids = allocationTable.objects.filter(student_1__className=className).values("project")
    allocated_projects = []
    print("allocated projects : ")
    for id in all_projects_ids:
        proj = project.objects.get(id=id["project"])
        print("id = ", id["project"])
        allocated_projects.append(proj)

    print("class ", className)
    # print("allocated projects\n",allocated_projects)
    avail_projects = []
    all_projects = project.objects.all()
    print("all projects")
    for proj in all_projects:
        print("id = ", proj.id)
        if proj not in allocated_projects:
            avail_projects.append(proj)
    
    print("available projects")
    for proj in avail_projects:
        print("id = ", proj.id)
        temp = {
            "title":proj.name ,
            "language":proj.language,
            "tech":proj.tech,
        }
        context["projects"].append(temp)
    
    rollNos = student.objects.all().values("rollNo").filter(className = className)
    rollNos = list(rollNos)
    temp = []
    for stu in rollNos:
        temp.append(str(stu["rollNo"]))
    
    context["rollNos"] = temp
    print(temp)
    return render(request, 'allocate_project.html',context)

def allocate_guides_groups(request, className="all"):
    context = {
        "css":"allocate_guide_group.css",
        "js":"allocate_guide_group.js",
    }

    if className == "all":
        context["classes"] = []
        classes = student.objects.all().values("className").distinct()
        for class_ in classes:
            context["classes"].append(class_["className"])
        return render(request, 'allocate_guide_group.html',context)
    elif request.method =="POST":
        guideName = request.POST["guideName"]

        all_allocation_entries = allocationTable.objects.all()
        
        for entry in all_allocation_entries:
            if entry.student_1.className == className:
                if request.POST.get(f"{entry.student_1.rollNo}", "NO") == "on":
                    guide_to_be_allocated = guide.objects.get(name=guideName)
                    entry_to_be_allocated = allocationTable.objects.get(student_1=entry.student_1)
                    entry_to_be_allocated.guide = guide_to_be_allocated
                    entry_to_be_allocated.save()
       

    context["css"]="allocate_guide_to_class.css"
    context["js"]="allocate_guide_to_class.js"
    context["guides"]=[]
    all_guides = guide.objects.all().values("name")
    for guide_ in all_guides:
        context["guides"].append(guide_["name"])
    
    all_allocation_entries = allocationTable.objects.all()
    context["students"] = []
    for entry in all_allocation_entries:
        if entry.student_1.className == className:
            temp = {
                "student_1_rollNo": entry.student_1.rollNo,
                "projectName": entry.project.name,
                "lang": entry.project.language,
                "allocated": entry.guide.name if entry.guide else "NO",
            }
            if entry.student_2:
                temp["student_2_rollNo"] = entry.student_2.rollNo
            context["students"].append(temp)
    
    return render(request, "allocate_guide_to_class.html", context)

    

def projectswise(request,className="all"):
    context = {
        "css":"allocate_project.css",
        
        "entries":[],
    }    
    if className == "all":
        # render the select_class_page.html
        context["css"] = "select_class_page.css"
        context["classes"] = []
        classes = student.objects.all().values("className").distinct()
        for class_ in classes:
            context["classes"].append(class_["className"])

        # print(context["classes"])
        return render(request, 'select_class_page.html',context)
    
    context["entries"] = get_allocation_data_classWise(className)
    return render(request, 'project_wise_view.html',context)

def guideswise(request, guideName='all'):
    context = {
        "css":"allocate_project.css",
        "entries":[],
    }
    if guideName == 'all':
        context["css"] = "select_guide_page.css"
        context["guides"] = []
        guides = guide.objects.all().values("name")
        for guide_ in guides:
            context["guides"].append(guide_["name"])

        return render(request, "select_guide_page.html",context)

    context["entries"] = get_allocation_data_guideWise(guideName)

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
        messages.info(request, 'Project description has been changed successfully!')
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
                    
                    # this checks if the rollNo1 already allocated a project or not
                    try:
                        does_exist = allocationTable.objects.get(
                            student_1__rollNo = form["rollNo1"]
                        )
                        return "Roll No 1 is already allocated a project"
                    except:
                        try:
                            does_exist = allocationTable.objects.get(
                                student_2__rollNo = form["rollNo1"]
                            )
                            return "Roll No 1 is already allocated a project"
                        except:
                            pass

                    # this checks if the rollNo2 already allocated a project or not
                    try:
                        does_exist = allocationTable.objects.get(
                            student_1__rollNo = form["rollNo2"]
                        )
                        return "Roll No 2 is already allocated a project"
                    except:
                        try:
                            does_exist = allocationTable.objects.get(
                                student_2__rollNo = form["rollNo2"]
                            )
                            return "Roll No 2 is already allocated a project"
                        except:
                            pass
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
            
            try:
                does_exist = allocationTable.objects.get(
                    student_1__rollNo = form["rollNo1"]
                )
                return "Roll No 1 is already allocated a project"
            except:
                pass
        else:
            return "Invalid RollNo2"
    else : 
        return "Invalid RollNO1"
    

    
    # ? and doing this will not break the code because we are only showing those options which are already registered in the projects
    check_project = project.objects.get(
        name=form["project_title"]
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
            student_1__className = form["className"],
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

def get_allocation_data_classWise(className):
    entries = []
    all_allocation_data = allocationTable.objects.all().filter(student_1__className=className).order_by("project")
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

def get_allocation_data_guideWise(guideName):
    entries = []
    all_allocation_data = allocationTable.objects.all().filter(guide__name="Mandeep Singh").order_by("student_1__className")
    for entry in all_allocation_data:
        temp = {
            "className": entry.student_1.className,
            "session": entry.student_1.session,
            "student_1" : {
                "rollNo": entry.student_1.rollNo,
                "name": entry.student_1.name,
                "email": entry.student_1.email,
                "mobile1": entry.student_1.mobile_1,
                "mobile2": entry.student_1.mobile_2,
            }
        }

        if entry.student_2:
            temp["student_2"] = {
                "rollNo": entry.student_2.rollNo,
                "name": entry.student_2.name,
                "email": entry.student_2.email,
                "mobile1": entry.student_2.mobile_1,
                "mobile2": entry.student_2.mobile_2,
            }
        else:
            temp["student_2"] = None
        
        temp["guide"] = {
                "name": entry.guide.name
            }
        
        temp["project"]={
            "name": entry.project.name,
            "lang": entry.project.language,
        }

        entries.append(temp)