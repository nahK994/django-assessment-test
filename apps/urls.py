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
from apps.company_management_app.views import CompanyViewset
from apps.employee_management_app.views import EmployeeViewset
from apps.device_management_app.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url


router = DefaultRouter()

base_company_url = "api/companies"
router.register(base_company_url, CompanyViewset, basename="company")

base_employee_url = "api/employees"
router.register(base_employee_url, EmployeeViewset, basename="employee")

base_device_url = "api/devices"
router.register(base_device_url, DeviceViewset, basename="device")

url_patterns = router.urls + [
    url(base_device_url+'/<str:device_id>/employees/<int:employee_id>/allot', allot_device_for_employee),
    url(base_device_url+'/<str:device_id>/employees/<int:employee_id>/deallot', deallot_device_for_employee),
]

schema_view = get_swagger_view(title='Config Management Services API', patterns=url_patterns)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(base_company_url+'/', include('apps.company_management_app.urls')),
    path(base_employee_url+'/', include('apps.employee_management_app.urls')),
    path(base_device_url+'/', include('apps.device_management_app.urls')),
    url('api/docs', schema_view)
]
