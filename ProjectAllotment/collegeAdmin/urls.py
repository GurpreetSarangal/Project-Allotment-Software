from django.urls import path

from . import views

urlpatterns = [
    path('', views.adminDashboard, name='adminDashboard'),
    path('allstaff/', views.staffview, name="all_staff"),
    path('allguides/', views.all_guide, name="all_guide"),
    path('addguides/', views.add_guide, name="add_guide"),
    path('allguides/<int:id>', views.edit_guide, name="edit_guide"),
    path('allguides/delete/<int:id>', views.delete_guide, name="delete_guide"),
    path('sessions/', views.sessionsview, name="sessions"),
    path('class/', views.classview, name="class"),
]