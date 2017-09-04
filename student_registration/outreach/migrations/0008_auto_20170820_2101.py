# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-20 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0007_auto_20170809_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='family_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('engaged', 'Engaged'), ('divorced', 'Divorced'), ('widower', 'Widower'), ('single', 'Single')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='have_children',
            field=models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='p_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]