# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-01 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0023_auto_20171114_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='first_name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0627\u0648\u0644'),
        ),
    ]