from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", CompanyTypeViewset, basename="company")

urlpatterns = router.urls
