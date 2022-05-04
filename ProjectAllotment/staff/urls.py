from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.dashboard, name="home"),
    path('allocateprojects/<className>', views.allocate_project, name="allocate-project"),
    path('allocateguidesgroups/<className>', views.allocate_guides_groups, name="allocate-guide-group"),
    path('projectwise/<className>', views.projectswise, name="project-wise-table"),
    path('guidewise/<guideName>', views.guideswise, name="guide-wise-table"),
    path('allprojects/', views.all_projects, name="all-project"),
    path('addprojects/', views.add_projects, name="add-project"),
    path('editproject/<int:id>/', views.edit_projects, name="edit-project"),
    path('editproject/delete/<int:id>/', views.delete_projects, name="delete-project"),

]