# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-19 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0086_auto_20170406_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='type',
            field=models.CharField(blank=True, choices=[('first', 'first'), ('second', 'second'), ('other', '\u0622\u062e\u0631')], max_length=20, null=True),
        ),
    ]