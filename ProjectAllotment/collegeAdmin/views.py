from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def adminDashboard(request):
    context = {
        "heading":"Welcome, "+"Admin.name",
        "css": "dashboard"
    }
    return render(request, "collegeAdmin/dashboard.html", context)

def staffview(request):
    
    context = {
        "heading":"CSE Dept, Staff",
        "css":"staff",
        "staff":[
            {
                "name":"staff1",
                "phone":"9893849839",
                "email":"kadfkad@gkjd.com",
            },
            {
                "name":"staff2",
                "phone":"9893849839",
                "email":"kjadkfjakdj@gkjd.com",
            },
            {
                "name":"staff3",
                "phone":"8349898323",
                "email":"jkjqeqeqer@gkjd.com",
            },
        ]
    }
    return render(request, "collegeAdmin/editStaff.html", context)
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