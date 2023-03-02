from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", EmployeeViewset, basename="employee")

urlpatterns = router.urls
