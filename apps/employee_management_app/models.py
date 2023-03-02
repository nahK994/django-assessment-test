from django.db import models
from apps.company_management_app.models import Company


class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, related_name="employees", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Employees"
        db_table = "employee"
