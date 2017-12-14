# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-22 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0030_enrollment_outreach_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='student_outreached',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=50, null=True),
        ),
    ]