# Generated by Django 4.2.1 on 2023-05-27 17:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("geo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="geom",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]
