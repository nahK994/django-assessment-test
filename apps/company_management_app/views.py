from .serializers import CompanySerializer
from .models import Company
from rest_framework import viewsets
from utils.mixins import ModelManagerMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.device_management_app.models import Device
from apps.device_management_app.serializers import DeviceSerializer


class CompanyViewset(ModelManagerMixin, viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


@api_view(['GET'])
def get_company_devices(request, company_id):
    filtered_company = Company.objects.filter(id=company_id)
    if not filtered_company:
        return Response("no such company", status=status.HTTP_404_NOT_FOUND)
    
    company = filtered_company[0]
    filtered_devices = DeviceSerializer(company.devices, many=True)
    return Response(filtered_devices.data, status=status.HTTP_200_OK)