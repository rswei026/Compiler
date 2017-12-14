# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-08 06:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0018_attendance_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='students',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='students.Student'),
        ),
    ]