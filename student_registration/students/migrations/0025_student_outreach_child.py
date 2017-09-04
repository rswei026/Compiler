# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-08 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0006_auto_20170808_1334'),
        ('students', '0024_remove_student_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='outreach_child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outreach.Child'),
        ),
    ]