# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-15 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0019_auto_20170209_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='alpround',
            name='current_post_test',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alpround',
            name='current_pre_test',
            field=models.BooleanField(default=False),
        ),
    ]
