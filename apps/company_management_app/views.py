from .serializers import CompanySerializer
from .models import Company
from rest_framework import viewsets
from utils.mixins import ModelManagerMixin


class CompanyViewset(ModelManagerMixin, viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
