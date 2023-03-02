from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", CompanyViewset, basename="company")

urlpatterns = router.urls + [
    path('<int:company_id>/devices', get_company_devices),
]