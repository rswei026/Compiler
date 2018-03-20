# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-19 13:52
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0046_crossmatching_education_level'),
        ('outreach', '0033_remove_child_education_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0627\u0648\u0644')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='\u0627\u0644\u0634\u0647\u0631\u0629')),
                ('father_name', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='\u0627\u0633\u0645 \u0627\u0644\u0627\u0628')),
                ('mother_fullname', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='\u0627\u0633\u0645 \u0627\u0644\u0623\u0645 \u0648\u0634\u0647\u0631\u062a\u0647\u0627 ')),
                ('mother_firstname', models.CharField(blank=True, max_length=64, null=True)),
                ('mother_lastname', models.CharField(blank=True, max_length=64, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', '\u0630\u0643\u0631'), ('Female', '\u0627\u0646\u062b\u0649')], max_length=50, null=True, verbose_name='\u0627\u0644\u062c\u0646\u0633')),
                ('birthday_year', models.CharField(blank=True, choices=[(b'1990', 1990), (b'1991', 1991), (b'1992', 1992), (b'1993', 1993), (b'1994', 1994), (b'1995', 1995), (b'1996', 1996), (b'1997', 1997), (b'1998', 1998), (b'1999', 1999), (b'2000', 2000), (b'2001', 2001), (b'2002', 2002), (b'2003', 2003), (b'2004', 2004), (b'2005', 2005), (b'2006', 2006), (b'2007', 2007), (b'2008', 2008), (b'2009', 2009), (b'2010', 2010), (b'2011', 2011), (b'2012', 2012), (b'2013', 2013), (b'2014', 2014), (b'2015', 2015), (b'2016', 2016), (b'2017', 2017), (b'2018', 2018), (b'2019', 2019), (b'2020', 2020), (b'2021', 2021), (b'2022', 2022), (b'2023', 2023), (b'2024', 2024), (b'2025', 2025), (b'2026', 2026), (b'2027', 2027), (b'2028', 2028), (b'2029', 2029), (b'2030', 2030), (b'2031', 2031), (b'2032', 2032), (b'2033', 2033), (b'2034', 2034), (b'2035', 2035), (b'2036', 2036), (b'2037', 2037), (b'2038', 2038), (b'2039', 2039), (b'2040', 2040), (b'2041', 2041), (b'2042', 2042), (b'2043', 2043), (b'2044', 2044), (b'2045', 2045), (b'2046', 2046), (b'2047', 2047), (b'2048', 2048), (b'2049', 2049)], default=0, max_length=4, null=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0648\u0644\u0627\u062f\u0629 - \u0627\u0644\u0633\u0646\u0629')),
                ('birthday_month', models.CharField(blank=True, choices=[('1', '\u0643\u0627\u0646\u0648\u0646 \u0627\u0644\u062b\u0627\u0646\u064a'), ('2', '\u0634\u0628\u0627\u0637'), ('3', '\u0622\u0630\u0627\u0631'), ('4', '\u0646\u064a\u0633\u0627\u0646'), ('5', '\u0623\u064a\u0627\u0631'), ('6', '\u062d\u0632\u064a\u0631\u0627\u0646'), ('7', '\u062a\u0645\u0648\u0632'), ('8', '\u0622\u0628'), ('9', '\u0623\u064a\u0644\u0648\u0644'), ('10', '\u062a\u0634\u0631\u064a\u0646 \u0627\u0644\u0623\u0648\u0644'), ('11', '\u062a\u0634\u0631\u064a\u0646 \u0627\u0644\u062b\u0627\u0646\u064a'), ('12', '\u0643\u0627\u0646\u0648\u0646 \u0627\u0644\u0623\u0648\u0644')], default=0, max_length=2, null=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0648\u0644\u0627\u062f\u0629 - \u0627\u0644\u0634\u0647\u0631')),
                ('birthday_day', models.CharField(blank=True, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5), (b'6', 6), (b'7', 7), (b'8', 8), (b'9', 9), (b'10', 10), (b'11', 11), (b'12', 12), (b'13', 13), (b'14', 14), (b'15', 15), (b'16', 16), (b'17', 17), (b'18', 18), (b'19', 19), (b'20', 20), (b'21', 21), (b'22', 22), (b'23', 23), (b'24', 24), (b'25', 25), (b'26', 26), (b'27', 27), (b'28', 28), (b'29', 29), (b'30', 30), (b'31', 31)], default=0, max_length=2, null=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0648\u0644\u0627\u062f\u0629 - \u0627\u0644\u064a\u0648\u0645')),
                ('place_of_birth', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0645\u0643\u0627\u0646 \u0627\u0644\u0648\u0644\u0627\u062f\u0629 ')),
                ('family_status', models.CharField(blank=True, choices=[('married', '\u0645\u062a\u0632\u0648\u062c / \u0645\u062a\u0632\u0648\u062c\u0629'), ('engaged', '\u0645\u062e\u0637\u0648\u0628 / \u0645\u062e\u0637\u0648\u0628\u0629'), ('divorced', '\u0645\u0637\u0644\u0642 / \u0645\u0637\u0644\u0642\u0629'), ('widower', '\u0627\u0631\u0645\u0644 / \u0627\u0631\u0645\u0644\u0629'), ('single', '\u0623\u0639\u0632\u0628 / \u0639\u0632\u0628\u0627\u0621')], max_length=50, null=True, verbose_name='\u0648\u0636\u0639 \u0627\u0644\u062a\u0644\u0645\u064a\u0630')),
                ('have_children', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True, verbose_name='\u0644\u062f\u064a\u0647 \u0627\u0637\u0641\u0627\u0644')),
                ('phone', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u0627\u0644\u0647\u0627\u062a\u0641')),
                ('phone_prefix', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u0631\u0645\u0632 \u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641 ')),
                ('registered_in_unhcr', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True, verbose_name='\u0645\u0633\u062c\u0644 \u0644\u062f\u0649 \u0627\u0644\u0645\u0641\u0648\u0636\u064a\u0629')),
                ('id_number', models.CharField(blank=True, db_index=True, max_length=45, null=True, verbose_name='\u0631\u0642\u0645 \u0627\u0644\u0628\u0637\u0627\u0642\u0629')),
                ('address', models.TextField(blank=True, null=True, verbose_name='\u0627\u0644\u0639\u0646\u0648\u0627\u0646')),
                ('p_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='P-code')),
                ('number', models.CharField(blank=True, max_length=45, null=True)),
                ('number_part1', models.CharField(blank=True, max_length=45, null=True)),
                ('number_part2', models.CharField(blank=True, max_length=45, null=True)),
                ('form_id', models.CharField(blank=True, max_length=45, null=True)),
                ('formid_ind', models.CharField(blank=True, max_length=45, null=True)),
                ('barcode_subset', models.CharField(blank=True, db_index=True, max_length=45, null=True)),
                ('calculated_age', models.CharField(blank=True, max_length=45, null=True)),
                ('current_situation', models.CharField(blank=True, choices=[('1', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('2', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('3', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('4', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('5', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('6', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629'), ('7', '\u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u062f\u0631\u0627\u0633\u064a\u0629')], max_length=50, null=True)),
                ('last_edu_system', models.CharField(blank=True, max_length=200, null=True)),
                ('last_school_formal_year', models.CharField(blank=True, max_length=45, null=True)),
                ('last_education_year', models.CharField(blank=True, max_length=45, null=True)),
                ('last_public_school_location', models.CharField(blank=True, choices=[('Leb', 'Lebanon'), ('Syr', 'Syria'), ('Irq', 'Iraq'), ('Other', '\u0622\u062e\u0631')], max_length=50, null=True)),
                ('last_informal_education', models.CharField(blank=True, choices=[('ALP', 'ALP'), ('BLN', 'BLN'), ('CB-ECE', 'CB-ECE'), ('SALP', 'SALP'), ('Prep.ALP', 'Prep.ALP'), ('Special_EDU_Dis', 'Special_EDU_Dis')], max_length=50, null=True)),
                ('not_enrolled_reasons', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('1', '\u0627\u0644\u0633\u0628\u0628'), ('2', '\u0627\u0644\u0633\u0628\u0628'), ('3', '\u0627\u0644\u0633\u0628\u0628'), ('4', '\u0627\u0644\u0633\u0628\u0628'), ('5', '\u0627\u0644\u0633\u0628\u0628'), ('6', '\u0627\u0644\u0633\u0628\u0628'), ('7', '\u0627\u0644\u0633\u0628\u0628'), ('8', '\u0627\u0644\u0633\u0628\u0628'), ('9', '\u0627\u0644\u0633\u0628\u0628'), ('10', '\u0627\u0644\u0633\u0628\u0628'), ('11', '\u0627\u0644\u0633\u0628\u0628'), ('12', '\u0627\u0644\u0633\u0628\u0628'), ('13', '\u0627\u0644\u0633\u0628\u0628'), ('14', '\u0627\u0644\u0633\u0628\u0628'), ('15', '\u0627\u0644\u0633\u0628\u0628'), ('16', '\u0627\u0644\u0633\u0628\u0628'), ('17', '\u0627\u0644\u0633\u0628\u0628'), ('18', '\u0627\u0644\u0633\u0628\u0628')], max_length=50, null=True), blank=True, null=True, size=None)),
                ('consent_child_protection', models.CharField(blank=True, choices=[('Yes', '\u0646\u0639\u0645'), ('No', '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('work_type', models.CharField(blank=True, max_length=100, null=True)),
                ('disability_type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('Walking', 'Walking'), ('Seeing', 'Seeing'), ('Hearing', 'Hearing'), ('Speaking', 'Speaking'), ('Self_Care', 'Self Care'), ('Learning', 'Learning'), ('Interacting', 'Interacting'), ('Other', '\u0622\u062e\u0631')], max_length=50, null=True), blank=True, null=True, size=None)),
                ('disability_note', models.CharField(blank=True, max_length=100, null=True)),
                ('other_disability_note', models.CharField(blank=True, max_length=100, null=True)),
                ('disability_comments', models.CharField(blank=True, max_length=200, null=True)),
                ('school_name', models.CharField(blank=True, max_length=200, null=True)),
                ('retention_support', models.CharField(blank=True, choices=[('1', 'Retention Support 1'), ('2', 'Retention Support 2'), ('3', 'Retention Support 3'), ('4', 'Retention Support 4'), ('5', 'Retention Support 5'), ('6', 'Retention Support 6')], max_length=50, null=True)),
                ('formal_education_type', models.CharField(blank=True, max_length=100, null=True)),
                ('formal_education_shift', models.CharField(blank=True, choices=[('KG', 'KG'), ('First', '\u062f\u0648\u0627\u0645 \u0635\u0628\u0627\u062d\u064a'), ('Second', '\u062f\u0648\u0627\u0645 \u0628\u0639\u062f \u0627\u0644\u0638\u0647\u0631'), ('ECE', 'ECE'), ('TVET', 'TVET')], max_length=50, null=True)),
                ('informal_education_type', models.CharField(blank=True, choices=[('ALP', 'ALP'), ('BLN', 'BLN'), ('CBECE', 'CB-ECE'), ('SALP', 'SALP')], max_length=50, null=True)),
                ('referred_school', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_school_first', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_school_second', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_school_alp', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_org', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_org_bln', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_org_ece', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_school_name', models.CharField(blank=True, max_length=200, null=True)),
                ('referred_org_name', models.CharField(blank=True, max_length=200, null=True)),
                ('referral_reason', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('1', 'Referral_Reason 1'), ('2', 'Referral_Reason 2'), ('3', 'Referral_Reason 3'), ('4', 'Referral_Reason 4'), ('5', 'Referral_Reason 5'), ('6', 'Referral_Reason 6'), ('7', 'Referral_Reason 7'), ('8', 'Referral_Reason 8'), ('9', 'Referral_Reason 9'), ('10', 'Referral_Reason 10'), ('11', 'Referral_Reason 11'), ('12', 'Referral_Reason 12'), ('13', 'Referral_Reason 13'), ('14', 'Referral_Reason 14'), ('15', 'Referral_Reason 15')], max_length=50, null=True), blank=True, null=True, size=None)),
                ('referral_note', models.CharField(blank=True, max_length=200, null=True)),
                ('household', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outreach_children2', to='outreach.HouseHold')),
                ('id_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.IDType', verbose_name='\u0646\u0648\u0639 \u0627\u0644\u0628\u0637\u0627\u0642\u0629')),
                ('mother_nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality', verbose_name='\u062c\u0646\u0633\u064a\u0629 \u0627\u0644\u0623\u0645')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Nationality', verbose_name=' \u0627\u0644\u062c\u0646\u0633\u064a\u0629')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
