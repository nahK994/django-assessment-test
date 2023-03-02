from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", DeviceViewset, basename="device")

urlpatterns = router.urls
