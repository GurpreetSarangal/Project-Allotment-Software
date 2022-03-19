
import string
from telnetlib import STATUS
from urllib.error import ContentTooShortError
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from . import getStudentsData
import logging
import pandas as pd
import re
import json



# Create your views here.
def adminDashboard(request):
    context = {
        "css": "admin_dashboard"
    }
    return render(request, "collegeAdmin/dashboard.html", context)

def staffview(request):
    temp_user = User.objects.all()
    data={
        "css":"staff",
        "users":[],
    }
    for u in temp_user:
        temp={}
        temp["username"]=(u.username)
        temp["email"]=(u.email)
        data["users"].append(temp)
    
    return render(request, "collegeAdmin/all_staff.html", data)
    

def all_guide(request):
    context = {
        "css":"all_guide",
        "users": []
    }

    all_guides = guide.objects.all()
    for one_guide in all_guides:
        temp = {
            "id":one_guide.id,
            "username":one_guide.name,
            "email":one_guide.email,
            "mobile1":one_guide.mobile_1,
            "mobile2":one_guide.mobile_2,
        }
        context["users"].append(temp)
    return render(request, "collegeAdmin/all_guide.html",context)

def add_guide(request):
    context={
        "css":"add_guide",
        
    }

    if(request.method == "POST"):
        new_details = {
        "guide_name" : request.POST["guide_name"],
        "mobile_1" : request.POST["mobile1"],
        "mobile_2" : request.POST["mobile2"],
        "email" : request.POST["email"],
        }
        new_guide = validate_inputs(request, new_details)
        if new_guide != None:
            new_guide.save()
            messages.info(request, 'New guide has been added successfully!')
       

        
    return render(request, 'collegeAdmin/add_guide.html',context)

def edit_guide(request, id):
    curr_guide = guide.objects.get(id=id)
    if request.method == "POST":
        new_details = {
            "id":id,
            "guide_name" : request.POST["guide_name"],
            "mobile_1" : request.POST["mobile1"],
            "mobile_2" : request.POST["mobile2"],
            "email" : request.POST["email"],
        }

        updated_guide = validate_inputs(request, new_details)
        if updated_guide != None:
            curr_guide=updated_guide
            curr_guide.save()
            messages.info(request, 'Details of Guide has been changed successfully!')
        

    context = {
        "css":'edit_guide',
        "user":{
            "id":curr_guide.id,
            "username":curr_guide.name,
            "mobile1":curr_guide.mobile_1,
            "mobile2":curr_guide.mobile_2,
            "email":curr_guide.email,
        }
    }


    return render(request, "collegeAdmin/edit_guide.html",context)

def delete_guide(request, id):
    guide.objects.get(id=id).delete()
    return redirect("all_guide")

def sessionsview(request):
    context = {
        "css" : "all_session",
        "js" : "all_session",
    }
    if is_ajax(request=request) and request.method == "GET":
        context["classes"] = []
        session = request.GET.get("curr_session")

        # print(session)
        session = f"{session}-{int(session)+1}"
        # print(session)
        classes = student.objects.filter(session=session).values("className").distinct()
        # print(classes)
        # classes is a query set but class_ will be a str which will be appended in "classes" array of context
        for class_ in classes:
            curr_class = {}
            curr_class["thisSession"] = session
            curr_class["className"] = class_["className"]
            curr_class["count"] = student.objects.filter(className=class_["className"]).values("rollNo").distinct().count()
            # print("class_ = ", class_)
            # print(curr_class)
            context["classes"].append(curr_class)
            # print(context["classes"])

        # print(context["classes"])
        # print("this is json",json.dumps(context["classes"]))

        response = json.dumps(context["classes"])
        return JsonResponse(response, status=200, safe=False)
    else:
        context["sessions"] = []
        all_session = student.objects.all().values("session").distinct()
        for session in all_session:
            session_obj = {}
            session_obj["id"] = re.split("-",str(session["session"]))[0]
            session_obj["title"] = session["session"]
            context["sessions"].append(session_obj)
            print(context["sessions"])
            
        return render(request, "collegeAdmin/all_session.html",context)
    

def classview(request, className):
    context = {
        "css" : "class_template",
        "js": "class_template",
        "rawURL": "/projectadmin/sessions/class/"+className,
        
    }
    session = re.split(" \| ", className)[0]
    className = re.split(" \| ", className)[1]

    context["curr_class"] = className
    context["curr_session"] = session
    context["No_of_students"] = student.objects.filter(className=className, session=session).count()

    all_students = student.objects.filter(className=className, session=session)
    context["all_students"] = []
    for stu in all_students:
        temp = {
            "rollNo": stu.rollNo,
            "name": stu.name,
            "fatherName" : stu.fatherName,
            "mobile_1": stu.mobile_1,
            "mobile_2": stu.mobile_2,
            "email": stu.email,
        }
        context["all_students"].append(temp)
        
    
    return render(request, "collegeAdmin/class_template.html", context)
  


# ! utility functions
'''
to call add a new class first select if you want to read a csv file or fetch
data from website 
if data is to be fetched from website then call 'getStudentsData.from_website(data)'
where data contains details of the class to be fetched. This function returns the 
`CSV_PATH` which is the path of new csv file which is to be passed to 'csv_to_django_db(csv_path)'
this function will read the csv and create records of new class.

and if data is read directly from csv file, first make sure that the order of details 
should always match with the documentations then specify the path of csv file 
and call 'insert_stu_details()'

currently available paths: 

    CSV_PATH = '/home/gurpreetsarangal/Documents/_StudyMaterial/Code/Selenium_tutorial/data/student/Bachelor of Computer Applications, Semester - V-2021.csv'

    CSV_PATH2 = '/home/gurpreetsarangal/Documents/_StudyMaterial/Code/Selenium_tutorial/data/student/B.Sc. (Information Technology), Semester - V-2021.csv'
'''


def insert_stu_details(csv_path):
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  

    logger=logging.getLogger("DataInserter")
    logger.setLevel(logging.DEBUG)

    data = pd.read_csv(csv_path)
    student_details = data.values
    print(student_details)
    for std in student_details:
        try:
            temp_student = student(
                session = std[0],
                rollNo = std[1],
                name = std[2],
                fatherName = std[3],
                className = std[4],
                email = std[5],
                mobile_1 = std[6],
                mobile_2 = std[7],
            )
        
        except:
            logger.error(f"student with rollno {std[1]} already existed")
            
        temp_student.save()

    logger.info(f"class has been added")


def csv_to_django_db(CSV_PATH):
    getStudentsData.formatData.format_csv(CSV_PATH)
    insert_stu_details(CSV_PATH)

# to validate emails
def is_valid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)

# to validate input data
def validate_inputs(request, obj):
    if not is_valid(obj["email"]):
        messages.error(request, 'No Email Provided')
        return None;

    if(obj["mobile_1"]=='' and obj["mobile_2"]==''):
        messages.error(request, 'No Mobile Number Provided')
        return None

    elif(obj["mobile_1"]==""):
        obj["mobile_1"] = 0
        try:
            new_guide = guide(
                id = obj["id"],
                name = obj["guide_name"],
                email = obj["email"],
                mobile_1 = obj["mobile_1"],
                mobile_2 = obj["mobile_2"],
                
            )
        except:
            new_guide = guide(
                name = obj["guide_name"],
                email = obj["email"],
                mobile_1 = obj["mobile_1"],
                mobile_2 = obj["mobile_2"],
            )
        return new_guide
        

    elif(obj["mobile_2"]==""):
        obj["mobile_2"] = 0
        try:
            new_guide = guide(
                id = obj["id"],
                name = obj["guide_name"],
                email = obj["email"],
                mobile_1 = obj["mobile_1"],
                mobile_2 = obj["mobile_2"],
                
            )
        except:
            new_guide = guide(
                name = obj["guide_name"],
                email = obj["email"],
                mobile_1 = obj["mobile_1"],
                mobile_2 = obj["mobile_2"],
                
            )

        return new_guide

    else:
        try:
            new_guide = guide(
                id = obj["id"],
                name = obj["guide_name"],
                email = obj["email"],
                mobile_1 = obj["mobile_1"],
                mobile_2 = obj["mobile_2"], 
            )
        except:
            new_guide = guide(
                name = obj["guide_name"],
                email = obj["email"],
                mobile_1 = obj["mobile_1"],
                mobile_2 = obj["mobile_2"],
                
            )
        return new_guide

# this is to check if request is ajax
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'