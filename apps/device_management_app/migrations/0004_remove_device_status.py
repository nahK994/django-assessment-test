# Generated by Django 3.2.15 on 2023-03-02 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management_app', '0003_rename_device_id_device_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='status',
        ),
    ]
