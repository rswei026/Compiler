# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-19 08:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0003_auto_20160517_1646'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attribute',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site'),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('site', 'slug')]),
        ),
    ]