# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-11 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0043_auto_20171103_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreach',
            name='new_registry',
            field=models.CharField(blank=True, choices=[('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=50, null=True, verbose_name='\u064a\u062a\u0645 \u0627\u0644\u062a\u0633\u062c\u064a\u0644 \u0644\u0627\u0648\u0644 \u0645\u0631\u0629\u061f'),
        ),
    ]
