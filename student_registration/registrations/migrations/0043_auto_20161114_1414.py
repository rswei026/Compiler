# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-14 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0042_auto_20161109_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wfpdistributionsite',
            options={'ordering': ['name'], 'verbose_name': 'WFP Distribution Site'},
        ),
    ]
