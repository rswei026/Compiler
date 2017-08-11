# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-16 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_alprefermatrix_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Education Year',
            },
        ),
    ]
