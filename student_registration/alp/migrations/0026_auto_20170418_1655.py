# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-18 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0025_outreach_dropout_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreach',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alp_school', to='schools.School'),
        ),
    ]