# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-28 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0044_auto_20180221_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crossmatching',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matched', to='outreach.Child'),
        ),
    ]
