# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-15 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0035_auto_20170915_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='outreach',
            name='post_test_room',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='outreach',
            name='pre_test_room',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]