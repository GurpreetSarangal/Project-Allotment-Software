from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminDashboard, name='index'),
    path('staff/', views.staffview, name="staff_url"),
    path('guides/', views.guidesview, name="guides_url"),
    path('sessions/', views.sessionsview, name="sessions_url"),
    path('class/', views.classview, name="class_url"),
]