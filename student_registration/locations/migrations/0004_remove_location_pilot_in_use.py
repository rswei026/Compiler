# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-08 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_location_pilot_in_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='pilot_in_use',
        ),
    ]