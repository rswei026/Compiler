# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-27 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0018_enrollment_moved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loggingstudentmove',
            options={'ordering': ['id'], 'verbose_name': 'Student moves logs', 'verbose_name_plural': 'Student moves logs'},
        ),
        migrations.AlterModelOptions(
            name='studentmove',
            options={'ordering': ['id'], 'verbose_name': 'Auto search student moves', 'verbose_name_plural': 'Auto search student moves'},
        ),
    ]
