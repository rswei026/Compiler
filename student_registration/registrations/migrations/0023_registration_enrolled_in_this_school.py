# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-07 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0022_auto_20160930_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='enrolled_in_this_school',
            field=models.BooleanField(default=True),
        ),
    ]
