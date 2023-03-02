from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", CompanyViewset, basename="company")

urlpatterns = router.urls
