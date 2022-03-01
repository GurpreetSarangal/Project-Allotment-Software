from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.dashboard, name="home"),
    path('allocateprojects/', views.allocate_project, name="allocate-project"),
    path('allocateguides', views.allocate_guides, name="allocate-guides"),
    path('allocategroups', views.allocate_groups, name="allocate-groups"),
    path('porjectsview', views.projectsview, name="projects-view"),
    path('guidesview', views.guidesview, name="guides-view"),
]