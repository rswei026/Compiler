# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-18 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clm', '0009_auto_20171018_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbece',
            name='site',
            field=models.CharField(blank=True, choices=[('in_school', ' \u062f\u0627\u062e\u0644 \u0627\u0644\u0645\u062f\u0631\u0633\u0629'), ('out_school', '\u062e\u0627\u0631\u062c \u0627\u0644\u0645\u062f\u0631\u0633\u0629')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rs',
            name='site',
            field=models.CharField(blank=True, choices=[('in_school', ' \u062f\u0627\u062e\u0644 \u0627\u0644\u0645\u062f\u0631\u0633\u0629'), ('out_school', '\u062e\u0627\u0631\u062c \u0627\u0644\u0645\u062f\u0631\u0633\u0629')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rs',
            name='type',
            field=models.CharField(blank=True, choices=[('homework_support', '\u062f\u0639\u0645 \u0627\u0644\u0648\u0627\u062c\u0628\u0627\u062a \u0627\u0644\u0645\u0646\u0632\u0644\u064a\u0629'), ('remedial_support', '\u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0639\u0644\u0627\u062c\u064a')], max_length=50, null=True),
        ),
    ]