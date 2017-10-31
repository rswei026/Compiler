# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-31 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winterization', '0004_auto_20171031_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='_rev',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='latitude',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='longitude',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='p_code',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='p_code_name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='site_type',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='cadastral',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='district',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='governorate',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='phone_number',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
