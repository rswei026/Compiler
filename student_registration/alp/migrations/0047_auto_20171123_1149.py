# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-23 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0046_auto_20171121_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='outreach',
            name='post_comment',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0645\u0644\u0627\u062d\u0627\u0638\u0627\u062a'),
        ),
        migrations.AddField(
            model_name='outreach',
            name='pre_comment',
            field=models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0645\u0644\u0627\u062d\u0627\u0638\u0627\u062a'),
        ),
    ]
