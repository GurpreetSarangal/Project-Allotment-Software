from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from . import getStudentsData
import logging
import pandas as pd



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
    
    return render(request, "collegeAdmin/editStaff.html", data)
    

def guidesview(request):
    return HttpResponse("this is guides")
    pass

def sessionsview(request):
    return HttpResponse("this is sessions")
    pass

def classview(request):
    return HttpResponse("this is class")
    pass


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