# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-14 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_auto_20161109_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=64L, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64L, null=True)),
                ('father_name', models.CharField(blank=True, max_length=64L, null=True)),
                ('mother_fullname', models.CharField(blank=True, max_length=64L, null=True)),
                ('birthday', models.CharField(blank=True, max_length=64L, null=True)),
                ('id_number', models.CharField(blank=True, max_length=100L, null=True)),
                ('number', models.CharField(blank=True, max_length=45L, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', '\u0630\u0643\u0631'), ('Female', '\u0627\u0646\u062b\u0649')], max_length=50, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='idtype',
            options={'ordering': ['id'], 'verbose_name': 'ID Type'},
        ),
        migrations.AlterModelOptions(
            name='nationality',
            options={'ordering': ['id'], 'verbose_name_plural': 'Nationalities'},
        ),
    ]