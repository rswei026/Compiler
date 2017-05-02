# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import *
from .forms import OutreachForm
from .models import (
    Outreach,
    ALPRound,
)
from student_registration.schools.models import (
    School,
    EducationLevel,
)
from student_registration.locations.models import Location
from student_registration.users.models import User
from student_registration.students.models import Student
from django.db.models import Q
from django.db.models import Sum
from student_registration.attendances.tasks import set_app_attendances


class OutreachResource(resources.ModelResource):
    governorate = fields.Field(
        column_name='governorate',
        attribute='school',
        widget=ForeignKeyWidget(School, 'location_parent_name')
    )
    district = fields.Field(
        column_name='district',
        attribute='school',
        widget=ForeignKeyWidget(School, 'location_name')
    )

    student_age = fields.Field(column_name='Student age')
    exam_total = fields.Field(column_name='Total pre test')
    post_exam_total = fields.Field(column_name='Total post test')
    referred_to = fields.Field(column_name='Referred to level')
    passed_pre = fields.Field(column_name='Passed the Pre-test')
    passed_post = fields.Field(column_name='Passed the Post-test')
    re_enrolled = fields.Field(column_name='Re-enrolled')

    class Meta:
        model = Outreach
        fields = (
            'id',
            'student__id',
            'student__id_type',
            'student__id_number',
            'student__number',
            'student__first_name',
            'student__father_name',
            'student__last_name',
            'student__mother_fullname',
            'student__birthday_year',
            'student__birthday_month',
            'student__birthday_day',
            'student_age',
            'student__sex',
            'student__nationality__name',
            'student__phone_prefix',
            'student__phone',
            'student__address',
            'governorate',
            'district',
            'school__number',
            'school__name',
            'level__name',
            'exam_result_arabic',
            'exam_result_language',
            'exam_result_math',
            'exam_result_science',
            'exam_total',
            'passed_pre',
            'exam_corrector_arabic',
            'exam_corrector_language',
            'exam_corrector_math',
            'exam_corrector_science',
            'assigned_to_level__name',
            'registered_in_level__name',
            'section__name',
            'post_exam_result_arabic',
            'post_exam_result_language',
            'post_exam_result_math',
            'post_exam_result_science',
            'post_exam_total',
            'post_exam_corrector_arabic',
            'post_exam_corrector_language',
            'post_exam_corrector_math',
            'post_exam_corrector_science',
            'referred_to',
            're_enrolled',
            'passed_post',
            'owner__username',
        )
        export_order = fields

    def dehydrate_student_age(self, obj):
        return obj.student_age

    def dehydrate_exam_total(self, obj):
        return obj.exam_total

    def dehydrate_post_exam_total(self, obj):
        return obj.post_exam_total

    def dehydrate_referred_to(self, obj):
        if obj.refer_to_level:
            if obj.refer_to_level_id == 1:
                if obj.post_exam_total >= 40:
                    if obj.registered_in_level_id < 9:
                        to_level = EducationLevel.objects.get(id=int(obj.registered_in_level_id) +1)
                        return to_level.name
                    else:
                        return obj.registered_in_level.name
                    # return 'Refer to ALP following level'
                # return 'Repeat ALP level/'+obj.registered_in_level.name
                return obj.registered_in_level.name
            else:
                return obj.refer_to_level.name

        return ''

    def dehydrate_passed_pre(self, obj):
        if obj.assigned_to_level:
            if obj.exam_total >= 40:
                return 'Yes'
        return 'No'

    def dehydrate_passed_post(self, obj):
        if obj.refer_to_level:
            if obj.post_exam_total >= 40:
                return 'Yes'
        return 'No'

    def dehydrate_re_enrolled(self, obj):
        return obj.student.alp_enrollment.count()


class PreTestTotalFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Pre test total'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'pre_test_total'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0', 'Equal 0'),
            ('1', 'More than 0')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            if self.value() == '0':
                return queryset.filter(
                    exam_result_arabic=0,
                    exam_result_language=0,
                    exam_result_math=0,
                    exam_result_science=0
                )
            else:
                return queryset.filter(
                    Q(exam_result_arabic__gt=0) |
                    Q(exam_result_language__gt=0) |
                    Q(exam_result_math__gt=0) |
                    Q(exam_result_science__gt=0)
                )
        return queryset


class PostTestTotalFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Post test total'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'post_test_total'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0', 'Equal 0'),
            ('1', 'More than 0')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            if self.value() == '0':
                return queryset.filter(
                    post_exam_result_arabic=0,
                    post_exam_result_language=0,
                    post_exam_result_math=0,
                    post_exam_result_science=0
                )
            else:
                return queryset.filter(
                    Q(post_exam_result_arabic__gt=0) |
                    Q(post_exam_result_language__gt=0) |
                    Q(post_exam_result_math__gt=0) |
                    Q(post_exam_result_science__gt=0)
                )
        return queryset


class GovernorateFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Governorate'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'governorate'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return ((l.id, l.name) for l in Location.objects.filter(type_id=1))

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(school__location__parent_id=self.value())
        return queryset


class RegisteredInLevelFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Have a level assigned?'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'registered_level'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('yes', 'Yes'),
            ('no', 'No')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() and self.value() == 'yes':
            return queryset.filter(registered_in_level__isnull=False)
        if self.value() and self.value() == 'no':
            return queryset.filter(registered_in_level__isnull=True)
        return queryset


class RegisteredInSectionFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Have a section assigned?'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'registered_section'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('yes', 'Yes'),
            ('no', 'No')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() and self.value() == 'yes':
            return queryset.filter(section__isnull=False)
        if self.value() and self.value() == 'no':
            return queryset.filter(section__isnull=True)
        return queryset


class OldNewFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Old or New?'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'old_new'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('old', 'Old'),
            ('new', 'New')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() and self.value() == 'new':
            return queryset.extra(where={
                'alp_outreach.student_id IN (Select distinct s.id from students_student s, alp_outreach e where s.id=e.student_id group by s.id having count(*) = 1)'
        }).distinct()
        if self.value() and self.value() == 'old':
            return queryset.extra(where={
                'alp_outreach.student_id IN (Select distinct s.id from students_student s, alp_outreach e where s.id=e.student_id group by s.id having count(*) > 1)'
            }).distinct()
        return queryset


class ReferredToFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Referred to'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'referred_to'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('alp', 'ALP'),
            ('alp1', 'Passed ALP level'),
            ('alp2', 'Repeat ALP level'),
            ('formal', 'Formal')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        post_test_round = ALPRound.objects.get(current_post_test=True)
        queryset = queryset.filter(alp_round=post_test_round)
        if self.value() and self.value() == 'alp':
            return queryset.filter(
                refer_to_level_id__in=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            )
        if self.value() and self.value() == 'alp1':
            return queryset.filter(
                refer_to_level_id__in=[2, 3, 4, 5, 6, 7, 8, 9]
            )
        if self.value() and self.value() == 'alp2':
            return queryset.filter(
                refer_to_level_id__in=[18, 19, 20, 21, 22, 23, 24, 25, 26]
            )
        if self.value() and self.value() == 'formal':
            return queryset.filter(
                refer_to_level_id__in=[1, 10, 11, 12, 13, 14, 15, 16, 17]
            )
        return queryset


class PassedTestFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Passed a test'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'passed_test'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('pre', 'Pre-test'),
            ('post', 'Post-test')
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() and self.value() == 'pre':
            pre_test_round = ALPRound.objects.get(current_pre_test=True)
            not_schools = User.objects.filter(groups__name__in=['PARTNER', 'CERD'])
            return queryset.filter(
                alp_round=pre_test_round,
                owner__in=not_schools,
                level__isnull=False,
                assigned_to_level__isnull=False,
            )
        if self.value() and self.value() == 'post':
            post_test_round = ALPRound.objects.get(current_post_test=True)
            return queryset.filter(
                alp_round=post_test_round,
                registered_in_level__isnull=False,
                refer_to_level__isnull=False
            )
        return queryset


class OutreachAdmin(ImportExportModelAdmin):
    resource_class = OutreachResource
    form = OutreachForm
    list_display = (
        'student',
        'student_age',
        'student_sex',
        'school',
        'caza',
        'governorate',
        'alp_round',
        'level',
        'total',
        'assigned_to_level',
        'registered_in_level',
        'section',
        'not_enrolled_in_this_school',
        're_enrolled',
        'created',
        'modified',
    )
    list_filter = (
        'alp_round',
        'school__number',
        'school',
        'school__location',
        GovernorateFilter,
        'level',
        'assigned_to_level',
        'registered_in_level',
        'section',
        'student__sex',
        'not_enrolled_in_this_school',
        RegisteredInLevelFilter,
        RegisteredInSectionFilter,
        'created',
        'modified',
    )
    search_fields = (
        'student__first_name',
        'student__father_name',
        'student__last_name',
        'student__mother_fullname',
        'school__name',
        'school__number',
        'student__id_number',
        'school__location__name',
        'level__name',
        'owner__username'
    )

    def get_queryset(self, request):
        qs = super(OutreachAdmin, self).get_queryset(request)
        return qs

    def caza(self, obj):
        if obj.school and obj.school.location:
            return obj.school.location.name
        return ''

    def governorate(self, obj):
        if obj.school and obj.school.location and obj.school.location.parent:
            return obj.school.location.parent.name
        return ''

    def total(self, obj):
        total = obj.exam_total
        if obj.level and obj.level.note:
            total = u'{}/{}'.format(
                str(total),
                str(obj.level.note)
            )
        return total

    def post_total(self, obj):
        total = obj.post_exam_total
        if obj.registered_in_level and obj.registered_in_level.note:
            total = u'{}/{}'.format(
                str(total),
                str(obj.registered_in_level.note)
            )
        return total

    def re_enrolled(self, obj):
        return obj.student.alp_enrollment.count()


class CurrentOutreach(Outreach):
    class Meta:
        proxy = True


class CurrentOutreachAdmin(OutreachAdmin):

    list_display = (
        'school',
        'caza',
        'governorate',
        'student_number',
        'student',
        'student_age',
        'student_sex',
        'student_nationality',
        'created',
        'modified',
    )

    list_filter = (
        'school',
        'school__location',
        GovernorateFilter,
        'student__sex',
        'student__nationality',
        'created',
        'modified',
    )

    def get_queryset(self, request):
        alp_round = ALPRound.objects.filter(current_pre_test=True)
        users = User.objects.filter(groups__name__in=['PARTNER'])
        qs = super(CurrentOutreachAdmin, self).get_queryset(request)
        return qs.filter(
            alp_round=alp_round,
            owner__in=users
        )


class PreTest(Outreach):
    class Meta:
        proxy = True


class PreTestAdmin(OutreachAdmin):

    list_display = (
        'student',
        'student_age',
        'student_sex',
        'school',
        'caza',
        'governorate',
        'level',
        'total',
        'assigned_to_level',
        'created',
        'modified',
    )
    list_filter = (
        'school',
        'school__location',
        GovernorateFilter,
        'level',
        'assigned_to_level',
        'student__sex',
        'exam_corrector_arabic',
        'exam_corrector_language',
        'exam_corrector_math',
        'exam_corrector_science',
        PreTestTotalFilter,
        'created',
        'modified',
    )

    def get_queryset(self, request):
        alp_round = ALPRound.objects.filter(current_pre_test=True)
        not_schools = User.objects.filter(groups__name__in=['PARTNER', 'CERD'])
        qs = super(PreTestAdmin, self).get_queryset(request)
        return qs.filter(
            alp_round=alp_round,
            owner__in=not_schools,
            level__isnull=False,
            assigned_to_level__isnull=False,
        )


class CurrentRound(Outreach):
    class Meta:
        proxy = True


class CurrentRoundAdmin(OutreachAdmin):

    list_display = (
        'student',
        'student_mother_fullname',
        'student_age',
        'student_birthday',
        'student_sex',
        'school',
        'caza',
        'governorate',
        'level',
        'total',
        'assigned_to_level',
        'registered_in_level',
        're_enrolled',
        'section',
        'owner',
        'created',
        'modified',
    )
    list_filter = (
        'school',
        'school__location',
        GovernorateFilter,
        OldNewFilter,
        PassedTestFilter,
        ReferredToFilter,
        'level',
        'assigned_to_level',
        'registered_in_level',
        'refer_to_level',
        'section',
        'student__sex',
        'created',
        'modified',
    )

    def student_mother_fullname(self, obj):
        if obj.student:
            return obj.student.mother_fullname
        return ''

    def student_birthday(self, obj):
        if obj.student:
            return obj.student.birthday
        return ''

    # actions = ('push_attendances',)

    def get_queryset(self, request):
        alp_round = ALPRound.objects.filter(current_round=True)
        qs = super(CurrentRoundAdmin, self).get_queryset(request)
        return qs.filter(
            alp_round=alp_round,
            registered_in_level__isnull=False,
        )

    # def push_attendances(self, request, queryset):
    #     if 'school__id__exact' in request.GET:
    #         school = School.objects.get(id=request.GET['school__id__exact'])
    #         set_app_attendances.delay(school_number=school.number, school_type='alp')


class PostTest(Outreach):
    class Meta:
        proxy = True


class PostTestAdmin(OutreachAdmin):

    list_display = (
        'student',
        'student_age',
        'student_sex',
        'school',
        'caza',
        'governorate',
        'registered_in_level',
        'post_total',
        'refer_to_level',
        'section',
        'created',
        'modified',
    )
    list_filter = (
        'school',
        'school__location',
        GovernorateFilter,
        'registered_in_level',
        'refer_to_level',
        'section',
        'student__sex',
        'post_exam_corrector_arabic',
        'post_exam_corrector_language',
        'post_exam_corrector_math',
        'post_exam_corrector_science',
        PostTestTotalFilter,
        'created',
        'modified',
    )

    def get_queryset(self, request):
        alp_round = ALPRound.objects.filter(current_post_test=True)
        qs = super(PostTestAdmin, self).get_queryset(request)
        return qs.filter(
            alp_round=alp_round,
            registered_in_level__isnull=False,
            refer_to_level__isnull=False
        )


# class ReEnrolled(Outreach):
#     class Meta:
#         proxy = True
#
#
# class ReEnrolledAdmin(OutreachAdmin):
#
#     list_display = (
#         'student',
#         'student_age',
#         'student_sex',
#         'school',
#         'caza',
#         'governorate',
#         'level',
#         'total',
#         'assigned_to_level',
#         'registered_in_level',
#         'section',
#         'created',
#         'modified',
#     )
#     list_filter = (
#         'school',
#         'school__location',
#         GovernorateFilter,
#         'level',
#         'assigned_to_level',
#         'registered_in_level',
#         'refer_to_level',
#         'section',
#         'student__sex',
#         'created',
#         'modified',
#     )
#
#     def get_queryset(self, request):
#         qs = super(ReEnrolledAdmin, self).get_queryset(request)
#         alp_round = ALPRound.objects.filter(current_round=True)
#         qs = qs.filter(
#             alp_round=alp_round,
#             registered_in_level__isnull=False,
#         ).extra(where={
#                 'alp_outreach.student_id IN (Select distinct s.id from students_student s, alp_outreach e where s.id=e.student_id group by s.id having count(*) > 1)'
#             }).distinct()
#
#         return qs
#
#
# class NewEnrolled(Outreach):
#     class Meta:
#         proxy = True
#
#
# class NewEnrolledAdmin(OutreachAdmin):
#
#     list_display = (
#         'student',
#         'student_age',
#         'student_sex',
#         'school',
#         'caza',
#         'governorate',
#         'level',
#         'total',
#         'assigned_to_level',
#         'registered_in_level',
#         'section',
#         'created',
#         'modified',
#     )
#     list_filter = (
#         'school',
#         'school__location',
#         GovernorateFilter,
#         'level',
#         'assigned_to_level',
#         'registered_in_level',
#         'refer_to_level',
#         'section',
#         'student__sex',
#         'created',
#         'modified',
#     )
#
#     def get_queryset(self, request):
#         qs = super(NewEnrolledAdmin, self).get_queryset(request)
#         alp_round = ALPRound.objects.filter(current_round=True)
#         qs = qs.filter(
#             alp_round=alp_round,
#             registered_in_level__isnull=False,
#         ).extra(where={
#                 'alp_outreach.student_id IN (Select distinct s.id from students_student s, alp_outreach e where s.id=e.student_id group by s.id having count(*) = 1)'
#         }).distinct()
#
#         return qs


admin.site.register(Outreach, OutreachAdmin)
admin.site.register(CurrentOutreach, CurrentOutreachAdmin)
admin.site.register(PreTest, PreTestAdmin)
admin.site.register(CurrentRound, CurrentRoundAdmin)
admin.site.register(PostTest, PostTestAdmin)
# admin.site.register(ReEnrolled, ReEnrolledAdmin)
# admin.site.register(NewEnrolled, NewEnrolledAdmin)
admin.site.register(ALPRound)
