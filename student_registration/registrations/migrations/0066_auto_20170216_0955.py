# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-16 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_idtype_inuse'),
        ('registrations', '0065_auto_20170216_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_id_number',
            field=models.CharField(blank=True, max_length=45L, null=True),
        ),
        migrations.AddField(
            model_name='registeringadult',
            name='beneficiary_changed_id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beneficiary_changed_id', to='students.IDType'),
        ),
    ]