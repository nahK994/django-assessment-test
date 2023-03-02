from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import viewsets
from utils.mixins import ModelManagerMixin


class EmployeeViewset(ModelManagerMixin, viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
