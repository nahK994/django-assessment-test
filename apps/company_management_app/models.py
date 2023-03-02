from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Companies"
        db_table = "company"
