from .serializers import DeviceSerializer
from .models import Device
from rest_framework import viewsets
from utils.mixins import ModelManagerMixin


class DeviceViewset(ModelManagerMixin, viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
