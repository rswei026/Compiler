# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-22 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0008_auto_20170118_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='absentee',
            name='validation_status',
            field=models.BooleanField(default=False),
        ),
    ]
