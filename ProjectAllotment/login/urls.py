from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]