# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-05 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0074_merge_20180329_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='disabled',
            field=models.BooleanField(default=False, verbose_name='Disabled?'),
        ),
    ]