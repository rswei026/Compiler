# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-13 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0014_attendancesynclog'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancesynclog',
            name='school_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
