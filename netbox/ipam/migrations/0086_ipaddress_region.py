# Generated by Django 4.2.10 on 2024-05-21 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0185_gfk_indexes'),
        ('ipam', '0085_remove_ipaddress_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ip_addresses', to='dcim.region'),
        ),
    ]