from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password/change/', views.reset_password, name='reset-password'),
]