from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    apply_job,
    basic_login,
    hello_api,
    job_list,
    register_user,
    JobViewSet,
    ApplicationViewSet,
    RegisterView
)

# Router for REST API endpoints
router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Simple function-based endpoints
    path("hello/", hello_api),
    path("register", register_user),   # basic register function
    path("login", basic_login),
    path("jobs", job_list),            # simple job list
    path("apply", apply_job),          # apply endpoint

    # REST API endpoints
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
]
