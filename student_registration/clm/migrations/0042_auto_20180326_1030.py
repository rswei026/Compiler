# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-26 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0041_cbece_final_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbece',
            name='final_grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
