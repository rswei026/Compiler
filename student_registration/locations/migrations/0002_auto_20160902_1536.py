# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-02 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='gateway',
            new_name='type',
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('name', 'type', 'p_code')]),
        ),
    ]
