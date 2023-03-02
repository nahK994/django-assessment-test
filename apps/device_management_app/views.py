from .serializers import DeviceSerializer
from .models import Device
from apps.employee_management_app.models import Employee
from rest_framework import viewsets
from utils.mixins import ModelManagerMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime


class DeviceViewset(ModelManagerMixin, viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


def check_employee(employee_id):
    filtered_employeee = Employee.objects.filter(id=employee_id)
    if not filtered_employeee:
        raise Exception("no such employee")
    
    return filtered_employeee


def check_device(device_id):
    filtered_device = Device.objects.filter(id=device_id)
    if not filtered_device:
        raise Exception("no such device")
    
    return filtered_device


@api_view(['PATCH'])
def allot_device_for_employee(request, device_id, employee_id):
    try:
        filtered_employee = check_employee(employee_id)
        filtered_device = check_device(device_id)

        device = filtered_device[0]
        employee = filtered_employee[0]

        if device.status == "assigned":
            raise Exception("device has already been assigned")
        if device.company != employee.company:
            raise Exception("employess doesn't belong to this company")
        
        device.assignee = employee
        device.status = "assigned"
        device.checked_in_time = datetime.datetime.now()
        device.log = request.data['log']
        device.save()

        return Response("allocated", status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def deallot_device_for_employee(request, device_id, employee_id):
    try:
        filtered_employee = check_employee(employee_id)
        filtered_device = check_device(device_id)

        device = filtered_device[0]
        employee = filtered_employee[0]

        if device.status == "not assigned":
            raise Exception("device isn't assigned")
        if device.assignee != employee:
            raise Exception("device is assigned to someone else")
        
        device.assignee = None
        device.status = "not assigned"
        device.checked_in_time = None
        device.return_time = datetime.datetime.now()
        device.log = request.data['log']
        device.save()

        return Response("deallocated", status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
