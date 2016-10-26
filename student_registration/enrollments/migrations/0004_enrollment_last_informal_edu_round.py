# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0005_auto_20161026_1318'),
        ('enrollments', '0003_auto_20161026_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='last_informal_edu_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='alp.ALPRound'),
        ),
    ]
