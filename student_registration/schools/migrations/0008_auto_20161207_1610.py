# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-07 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['number']},
        ),
    ]
