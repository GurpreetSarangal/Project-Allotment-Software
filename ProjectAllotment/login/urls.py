from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
]