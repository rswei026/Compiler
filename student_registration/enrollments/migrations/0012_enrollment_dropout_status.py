# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-04 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0011_auto_20170228_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='dropout_status',
            field=models.BooleanField(default=False),
        ),
    ]
