# Generated by Django 4.2.10 on 2024-05-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0074_remove_iprange_addresses'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefix',
            name='area_network',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
