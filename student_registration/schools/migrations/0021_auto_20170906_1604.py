# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0020_auto_20170906_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='holiday',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
