# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-27 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.CharField(blank=True, max_length=4L, null=True),
        ),
    ]
