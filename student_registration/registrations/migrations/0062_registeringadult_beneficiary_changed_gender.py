# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-15 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0061_registeringadult_household_suspended'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_gender',
            field=models.CharField(blank=True, choices=[('Male', '\u0630\u0643\u0631'), ('Female', '\u0627\u0646\u062b\u0649')], max_length=50, null=True),
        ),
    ]