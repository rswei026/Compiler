# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='app_password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(blank=True, to='locations.Location'),
        ),
    ]
