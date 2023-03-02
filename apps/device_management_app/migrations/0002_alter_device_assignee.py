# Generated by Django 3.2.15 on 2023-03-02 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0001_initial'),
        ('device_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='employee_management_app.employee'),
        ),
    ]