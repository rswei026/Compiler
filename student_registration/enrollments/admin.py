# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import *
import datetime

from .models import Enrollment, StudentMove, LoggingStudentMove
from .forms import EnrollmentForm
from student_registration.students.models import Student
from student_registration.schools.models import (
    School,
)
from student_registration.locations.models import Location
from student_registration.attendances.tasks import set_app_attendances


class EnrollmentResource(resources.ModelResource):
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

    class Meta:
        model = Enrollment
        form = EnrollmentForm
        fields = (
            'id',
            'student__id',
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
            'governorate',
            'district',
            'school__number',
            'school__name',
            'section__name',
            'classroom__name',
            'last_education_level__name',
            'last_education_year',
            'last_school_type',
            'last_school_shift',
            'last_school',
            'last_year_result',
            'participated_in_alp',
            'last_informal_edu_round__name',
            'last_informal_edu_level__name',
            'last_informal_edu_final_result__name',
        )
        export_order = fields

    def dehydrate_student_age(self, obj):
        return obj.student_age


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


class FromAgeFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'From Age'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'from_age'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return ((l, l) for l in range(0, 100))

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            now = datetime.datetime.now()
            return queryset.filter(student__birthday_year__lte=(now.year - int(self.value())))

        return queryset


class ToAgeFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'To Age'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'to_age'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return ((l, l) for l in range(0, 100))

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            now = datetime.datetime.now()
            return queryset.filter(student__birthday_year__gte=(now.year - int(self.value())))
        return queryset


class EnrollmentAdmin(ImportExportModelAdmin):
    resource_class = EnrollmentResource
    form = EnrollmentForm
    fields = (
        'student',
        'school',
        'section',
        'classroom',
        'owner',
        'status',
        'year',
        'enrolled_in_this_school',
        'registered_in_unhcr',
        'last_education_level',
        'last_school_type',
        'last_school_shift',
        'last_school',
        'last_education_year',
        'last_year_result',
        'participated_in_alp',
        'last_informal_edu_level',
        'last_informal_edu_round',
        'last_informal_edu_final_result',
        'deleted',
    )
    list_display = (
        'student',
        'student_age',
        'school',
        'caza',
        'governorate',
        'classroom',
        'section',
        'created',
        'modified',
    )
    list_filter = (
        'education_year',
        'school__number',
        'school',
        'school__location',
        GovernorateFilter,
        'classroom',
        'section',
        'student__sex',
        'registered_in_unhcr',
        'student__id_type',
        'last_education_level',
        'last_education_year',
        'last_school_type',
        'last_school_shift',
        'last_school',
        'last_year_result',
        'participated_in_alp',
        'last_informal_edu_round',
        'last_informal_edu_level',
        'last_informal_edu_final_result',
        FromAgeFilter,
        ToAgeFilter,
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
        'classroom__name',
        'owner__username',
    )

    actions = ('push_attendances',)

    def get_queryset(self, request):
        qs = super(EnrollmentAdmin, self).get_queryset(request)
        return qs.exclude(deleted=True)

    def caza(self, obj):
        if obj.school and obj.school.location:
            return obj.school.location.name
        return ''

    def governorate(self, obj):
        if obj.school and obj.school.location and obj.school.location.parent:
            return obj.school.location.parent.name
        return ''

    def push_attendances(self, request, queryset):
        if 'school__id__exact' in request.GET:
            school = School.objects.get(id=request.GET['school__id__exact'])
            set_app_attendances.delay(school_number=school.number)


class Dropout(Enrollment):
    class Meta:
        proxy = True


class DropoutAdmin(EnrollmentAdmin):

    def get_queryset(self, request):
        return Enrollment.drop_objects.all()


class StudentMoveResource(resources.ModelResource):

    class Meta:
        model = StudentMove
        fields = (
            'enrolment1__student__first_name',
            'enrolment1__student__father_name',
            'enrolment1__student__last_name',
            'enrolment1__student__mother_fullname',
            'school1__name',
            'enrolment2__student__first_name',
            'enrolment2__student__father_name',
            'enrolment2__student__last_name',
            'enrolment2__student__mother_fullname',
            'school2__name',
        )
        export_order = fields


class StudentMoveAdmin(ImportExportModelAdmin):
    resource_class = StudentMoveResource
    fields = ()

    list_display = (
        'enrolment1',
        'school1',
        'enrolment2',
        'school2',
    )

    list_filter = (
        'school1',
        'school2',
    )

    search_fields = (
        'enrolment1__student__first_name',
        'enrolment1__student__father_name',
        'enrolment1__student__last_name',
        'enrolment1__student__mother_fullname',
        'school1__name',
        'enrolment2__student__first_name',
        'enrolment2__student__father_name',
        'enrolment2__student__last_name',
        'enrolment2__student__mother_fullname',
        'school2__name',
    )


class LoggingStudentMoveResource(resources.ModelResource):

    class Meta:
        model = LoggingStudentMove
        fields = ()
        export_order = fields


class LoggingStudentMoveAdmin(ImportExportModelAdmin):
    resource_class = LoggingStudentMoveResource
    fields = ()

    list_display = (
        'student',
        # 'enrolment__clasroom',
        'school_from',
        'school_to',
    )

    list_filter = (
        'school_from',
        'school_to',
    )

    search_fields = (

    )


admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Dropout, DropoutAdmin)
admin.site.register(StudentMove, StudentMoveAdmin)
admin.site.register(LoggingStudentMove, LoggingStudentMoveAdmin)
