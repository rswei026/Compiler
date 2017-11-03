# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-31 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('file_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Exported file',
                'verbose_name_plural': 'Exported files',
            },
        ),
    ]