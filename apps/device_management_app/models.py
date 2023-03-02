from django.db import models
from apps.company_management_app.models import Company
from apps.employee_management_app.models import Employee


class Device(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    company = models.ForeignKey(Company, related_name="devices", on_delete=models.CASCADE)
    assignee = models.ForeignKey(Employee, related_name="assigned_to", on_delete=models.CASCADE, null=True, blank=True)
    log = models.CharField(max_length=500)
    checked_in_time = models.DateField(null=True, blank=True)
    return_time = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Devices"
        db_table = "device"
