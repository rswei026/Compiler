# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-27 10:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0037_auto_20170915_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreach',
            name='assigned_to_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationLevel', verbose_name='\u0646\u062a\u064a\u062c\u0629 \u0627\u0644 Pre-test'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='exam_language',
            field=models.CharField(blank=True, choices=[('english', '\u0627\u0644\u0627\u0646\u0643\u0644\u064a\u0632\u064a\u0629'), ('french', '\u0627\u0644\u0641\u0631\u0646\u0633\u064a\u0629')], max_length=50, null=True, verbose_name='\u0644\u063a\u0629 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='exam_result_arabic',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='\u0627\u0644\u0639\u0631\u0628\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='exam_result_language',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Foreign Language'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='exam_result_math',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='\u0631\u064a\u0627\u0636\u064a\u0627\u062a'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='exam_result_science',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='\u0639\u0644\u0648\u0645'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_education_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.ClassRoom', verbose_name=' \u0623\u0639\u0644\u0649 \u0645\u0633\u062a\u0648\u0649 \u062a\u0639\u0644\u064a\u0645 \u0648\u0635\u0644 \u0625\u0644\u064a\u0647 \u0627\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_education_year',
            field=models.CharField(blank=True, choices=[('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020')], max_length=10, null=True, verbose_name=' \u0622\u062e\u0631 \u0633\u0646\u0629 \u062f\u0631\u0627\u0633\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_informal_edu_final_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.ClassLevel', verbose_name='\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0633\u0627\u0628\u0642\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u063a\u064a\u0631 \u0646\u0638\u0627\u0645\u064a \u0644\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_informal_edu_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationLevel', verbose_name=' \u0623\u0639\u0644\u0649 \u0645\u0633\u062a\u0648\u0649 \u062a\u0639\u0644\u064a\u0645 \u0648\u0635\u0644 \u0625\u0644\u064a\u0647 \u0627\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_informal_edu_result',
            field=models.CharField(blank=True, choices=[('graduated', '\u0646\u0627\u062c\u062d/\u0629'), ('failed', '\u0645\u0639\u064a\u062f/\u0629')], max_length=50, null=True, verbose_name='\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0633\u0627\u0628\u0642\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u063a\u064a\u0631 \u0646\u0638\u0627\u0645\u064a \u0644\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_informal_edu_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='alp.ALPRound', verbose_name='\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0633\u0627\u0628\u0642\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u063a\u064a\u0631 \u0646\u0638\u0627\u0645\u064a \u0644\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_informal_edu_year',
            field=models.CharField(blank=True, choices=[('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020')], max_length=10, null=True, verbose_name='\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0633\u0627\u0628\u0642\u0629 \u0644\u0644\u062a\u0639\u0644\u064a\u0645 \u063a\u064a\u0631 \u0646\u0638\u0627\u0645\u064a \u0644\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='last_year_result',
            field=models.CharField(blank=True, choices=[('graduated', '\u0646\u0627\u062c\u062d/\u0629'), ('failed', '\u0645\u0639\u064a\u062f/\u0629')], max_length=50, null=True, verbose_name='\u0622\u062e\u0631 \u0646\u062a\u064a\u062c\u0629 \u062d\u0635\u0644 \u0639\u0644\u064a\u0647\u0627 '),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationLevel', verbose_name='\u0627\u0645\u062a\u062d\u0627\u0646 \u0627\u0644\u062f\u062e\u0648\u0644'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location', verbose_name='\u0627\u0644\u0645\u0648\u0642\u0639'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modifications', to=settings.AUTH_USER_MODEL, verbose_name='\u0627\u062e\u0631 \u062a\u0639\u062f\u064a\u0644 \u0645\u0646 \u0642\u0628\u0644'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='participated_in_alp',
            field=models.CharField(blank=True, choices=[('na', 'n/a'), ('yes', '\u0646\u0639\u0645'), ('no', '\u0643\u0644\u0627')], max_length=50, null=True, verbose_name='\u0627\u0646\u062a\u0633\u0628 \u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0649 \u0628\u0631\u0646\u0627\u0645\u062c ALP'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='post_exam_language',
            field=models.CharField(blank=True, choices=[('english', '\u0627\u0644\u0627\u0646\u0643\u0644\u064a\u0632\u064a\u0629'), ('french', '\u0627\u0644\u0641\u0631\u0646\u0633\u064a\u0629')], max_length=50, null=True, verbose_name='\u0644\u063a\u0629 \u0627\u0644\u0627\u0645\u062a\u062d\u0627\u0646'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='post_exam_result_arabic',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='\u0627\u0644\u0639\u0631\u0628\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='post_exam_result_language',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Foreign Language'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='post_exam_result_math',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='\u0631\u064a\u0627\u0636\u064a\u0627\u062a'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='post_exam_result_science',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='\u0639\u0644\u0648\u0645'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='post_test_room',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='\u063a\u0631\u0641\u0629 \u0627\u0645\u062a\u062d\u0627\u0646 \u0627\u0644\u062f\u062e\u0648\u0644'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='pre_test_room',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Pre-test room'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='refer_to_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.ClassLevel', verbose_name='\u0646\u062a\u064a\u062c\u0629 \u0627\u0644 Post-test'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='registered_in_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationLevel', verbose_name=' \u0627\u0644\u0645\u0633\u062a\u0648\u0649 \u0627\u0644\u062d\u0627\u0644\u064a'),
        ),
        migrations.AlterField(
            model_name='outreach',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.Section', verbose_name='\u0627\u0644\u0634\u0639\u0628\u0629 \u0627\u0644\u062d\u0627\u0644\u064a\u0629'),
        ),
    ]