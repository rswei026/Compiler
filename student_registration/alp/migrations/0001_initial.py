# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_squashed_0010_auto_20160531_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outreach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('governorate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Governorate')),
                ('last_class_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.ClassLevel')),
                ('last_education_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.EducationLevel')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.PartnerOrganization')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
