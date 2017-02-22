# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-15 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0062_registeringadult_beneficiary_changed_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaint_resolution_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='omplaint_status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('resolved', 'Resolved')], max_length=20, null=True),
        ),
    ]
