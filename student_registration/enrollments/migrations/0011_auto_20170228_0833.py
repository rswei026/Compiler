# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-28 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0010_auto_20170227_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='last_school_shift',
            field=models.CharField(blank=True, choices=[('first', '\u062f\u0648\u0627\u0645 \u0635\u0628\u0627\u062d\u064a'), ('second', '\u062f\u0648\u0627\u0645 \u0628\u0639\u062f \u0627\u0644\u0638\u0647\u0631')], max_length=50, null=True),
        ),
    ]
