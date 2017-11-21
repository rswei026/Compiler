# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-06 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_idtype_inuse'),
        ('registrations', '0075_householdnotfound'),
    ]

    operations = [
        migrations.RenameField(
            model_name='householdnotfound',
            old_name='mother_full_name',
            new_name='mother_firstname',
        ),
        migrations.RenameField(
            model_name='householdnotfound',
            old_name='gender',
            new_name='sex',
        ),
        migrations.RemoveField(
            model_name='householdnotfound',
            name='primary_phone',
        ),
        migrations.RemoveField(
            model_name='householdnotfound',
            name='primary_phone_answered',
        ),
        migrations.RemoveField(
            model_name='householdnotfound',
            name='relation_to_householdhead',
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='age',
            field=models.CharField(blank=True, max_length=4L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='complaint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='registrations.Complaint'),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='full_name',
            field=models.CharField(blank=True, max_length=225L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='mother_fullname',
            field=models.CharField(blank=True, max_length=64L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='mother_lastname',
            field=models.CharField(blank=True, max_length=64L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='mother_nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality'),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality'),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='number',
            field=models.CharField(blank=True, max_length=45L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='number_children_five_to_nine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='number_children_ten_to_seventeen',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='number_part1',
            field=models.CharField(blank=True, max_length=45L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='number_part2',
            field=models.CharField(blank=True, max_length=45L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='old_id_number',
            field=models.CharField(blank=True, max_length=45L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='old_id_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='phone',
            field=models.CharField(blank=True, max_length=64L, null=True),
        ),
        migrations.AddField(
            model_name='householdnotfound',
            name='phone_prefix',
            field=models.CharField(blank=True, max_length=10L, null=True),
        ),
        migrations.AlterField(
            model_name='householdnotfound',
            name='birthday_day',
            field=models.CharField(blank=True, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5), (b'6', 6), (b'7', 7), (b'8', 8), (b'9', 9), (b'10', 10), (b'11', 11), (b'12', 12), (b'13', 13), (b'14', 14), (b'15', 15), (b'16', 16), (b'17', 17), (b'18', 18), (b'19', 19), (b'20', 20), (b'21', 21), (b'22', 22), (b'23', 23), (b'24', 24), (b'25', 25), (b'26', 26), (b'27', 27), (b'28', 28), (b'29', 29), (b'30', 30), (b'31', 31), (b'32', 32)], default=0, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='householdnotfound',
            name='id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.IDType'),
        ),
    ]