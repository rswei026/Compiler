# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-09 12:42
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0012_auto_20170927_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='formal_education_type',
            field=models.CharField(blank=True, choices=[('1', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('2', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('3', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('4', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='id_number',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='\u0631\u0642\u0645 \u0627\u0644\u0628\u0637\u0627\u0642\u0629'),
        ),
        migrations.AlterField(
            model_name='child',
            name='not_enrolled_reasons',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('1', '\u0627\u0644\u0633\u0628\u0628'), ('2', '\u0627\u0644\u0633\u0628\u0628'), ('3', '\u0627\u0644\u0633\u0628\u0628'), ('4', '\u0627\u0644\u0633\u0628\u0628'), ('5', '\u0627\u0644\u0633\u0628\u0628'), ('6', '\u0627\u0644\u0633\u0628\u0628'), ('7', '\u0627\u0644\u0633\u0628\u0628'), ('8', '\u0627\u0644\u0633\u0628\u0628'), ('9', '\u0627\u0644\u0633\u0628\u0628'), ('10', '\u0627\u0644\u0633\u0628\u0628'), ('11', '\u0627\u0644\u0633\u0628\u0628'), ('12', '\u0627\u0644\u0633\u0628\u0628'), ('13', '\u0627\u0644\u0633\u0628\u0628'), ('14', '\u0627\u0644\u0633\u0628\u0628'), ('15', '\u0627\u0644\u0633\u0628\u0628'), ('16', '\u0627\u0644\u0633\u0628\u0628'), ('17', '\u0627\u0644\u0633\u0628\u0628'), ('18', '\u0627\u0644\u0633\u0628\u0628')], max_length=50, null=True), blank=True, null=True, size=None),
        ),
    ]