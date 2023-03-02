from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", DeviceViewset, basename="device")

urlpatterns = router.urls + [
    path('<str:device_id>/employees/<int:employee_id>/allot', allot_device_for_employee),
    path('<str:device_id>/employees/<int:employee_id>/deallot', deallot_device_for_employee)
]
