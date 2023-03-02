from rest_framework import serializers
from .models import Device
from rest_framework.validators import UniqueValidator


class DeviceSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(source='id', required = True, validators=[UniqueValidator(queryset=Device.objects.all())])

    class Meta:
        model = Device
        fields = ['device_id', 'type', 'model', 'status', 'company', 'assignee', 'log', 'checked_in_time', 'return_time']