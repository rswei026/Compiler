# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-01 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhvisit', '0012_auto_20170127_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='childvisit',
            name='child_absence_period',
            field=models.CharField(blank=True, choices=[('first', '5-10'), ('second', '10-20'), ('third', '20++'), ('never', 'Never Attended'), ('frequent', 'Frequently Absent')], max_length=50, null=True),
        ),
    ]
