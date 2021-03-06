# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-13 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0022_school_attendance_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='director_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='director_phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='field_coordinator_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='it_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='it_phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='land_phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
