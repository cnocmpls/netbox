# Generated by Django 4.2.10 on 2024-05-01 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0071_ipaddress_ip_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipaddress',
            name='ip_range',
        ),
    ]
