# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0010_auto_20160901_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeringadult',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]