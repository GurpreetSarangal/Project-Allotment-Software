from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.dashboard, name="home"),
    path('allocateprojects/', views.allocate_project, name="allocate-project"),
    path('allocateguidesgroups/', views.allocate_guides_groups, name="allocate-guide-group"),
    path('projectwise/', views.projectswise, name="project-wise-table"),
    path('guidewise/', views.guideswise, name="guide-wise-table"),
    path('addprojects/', views.add_projects, name="add-project"),
]