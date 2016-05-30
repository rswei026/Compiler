# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_partnerorganization'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Nationality'),
        ),
    ]
