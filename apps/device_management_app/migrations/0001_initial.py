# Generated by Django 3.2.15 on 2023-03-02 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_management_app', '0001_initial'),
        ('company_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('log', models.CharField(max_length=500)),
                ('checked_in_time', models.DateField(blank=True, null=True)),
                ('return_time', models.DateField(blank=True, null=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='employee_management_app.employee')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='company_management_app.company')),
            ],
            options={
                'verbose_name_plural': 'Devices',
                'db_table': 'device',
            },
        ),
    ]
