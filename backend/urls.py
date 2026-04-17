from django.contrib import admin
from django.urls import include, path
from .views import hello_api, register_user, basic_login, job_list, apply_job

urlpatterns = [
   
    path("", include("backend.urls"))
]
