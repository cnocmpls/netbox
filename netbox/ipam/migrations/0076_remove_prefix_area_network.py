# Generated by Django 4.2.10 on 2024-05-16 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0075_prefix_area_network'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prefix',
            name='area_network',
        ),
    ]
