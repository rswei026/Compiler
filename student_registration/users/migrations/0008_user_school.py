# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_auto_20160712_1643'),
        ('users', '0007_auto_20160613_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.School'),
        ),
    ]
