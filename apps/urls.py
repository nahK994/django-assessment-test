"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.company_management_app import views as company_views
from apps.employee_management_app import views as employee_views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url


router = DefaultRouter()

base_company_url = "api/company"
router.register(base_company_url, company_views.CompanyViewset, basename="company")

base_employee_url = "api/employee"
router.register(base_employee_url, employee_views.EmployeeViewset, basename="employee")

schema_view = get_swagger_view(title='Config Management Services API', patterns=router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(base_company_url+'/', include('apps.company_management_app.urls')),
    path(base_employee_url+'/', include('apps.employee_management_app.urls')),
    url('api/docs', schema_view)
]
