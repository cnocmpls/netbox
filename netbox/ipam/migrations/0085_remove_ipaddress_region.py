# Generated by Django 4.2.10 on 2024-05-21 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0084_ipaddress_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipaddress',
            name='region',
        ),
    ]
