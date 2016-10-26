# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0004_auto_20161025_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALPRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45L, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_informal_edu_final_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.ClassLevel'),
        ),
        migrations.AddField(
            model_name='outreach',
            name='last_informal_edu_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='alp.ALPRound'),
        ),
    ]
