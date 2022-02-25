from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminDashboard, name='index'),
    path('StaffView/', views.staffview, name="staff_url"),
    path('GuidesView/', views.guidesview, name="guides_url"),
    path('SessionsView/', views.sessionsview, name="sessions_url"),
    path('ClassView/', views.classview, name="class_url"),
]