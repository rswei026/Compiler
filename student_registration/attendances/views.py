# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import datetime
import json

from django.views import View
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy

from braces.views import GroupRequiredMixin
from rest_framework import viewsets, mixins, permissions
from rest_framework.generics import ListAPIView
from rest_framework import status

from django.utils.translation import ugettext as _
from import_export.formats import base_formats
from student_registration.schools.models import (
    School,
    Section,
    ClassRoom
)
from student_registration.users.utils import force_default_language
from .models import Attendance, Absentee
from .serializers import AttendanceSerializer, AbsenteeSerializer
from student_registration.enrollments.models import (
    Enrollment,
    EducationYear,
)


class AttendanceViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    model = Attendance
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            if self.request.user.school:
                return self.queryset.filter(school_id=self.request.user.school.id)
            else:
                return []

        return self.queryset

    def create(self, request, *args, **kwargs):
        """
        :return: JSON
        """
        try:
            instance = Attendance.objects.get(school=int(request.POST.get('school')),
                                              attendance_date=request.POST.get('attendance_date'))
            return JsonResponse({'status': status.HTTP_201_CREATED, 'data': instance.id})
        except Attendance.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.instance = serializer.save()
            return JsonResponse({'status': status.HTTP_201_CREATED, 'data': serializer.instance.id})

    def update(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return super(AttendanceViewSet, self).update(request)
        instance = self.model.objects.get(id=kwargs['pk'])
        data = json.loads(request.data.keys()[0], "utf-8")
        level_section = data.keys()[0]
        if not instance.students:
            instance.students = data
        else:
            instance.students[level_section] = data[level_section]
        instance.save()
        return JsonResponse({'status': status.HTTP_200_OK, 'data': instance.id})

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()

    def partial_update(self, request, *args, **kwargs):
        return super(AttendanceViewSet, self).partial_update(request)


class AttendanceView(LoginRequiredMixin,
                     GroupRequiredMixin,
                     ListView):

    model = Attendance
    template_name = 'attendances/school.html'
    group_required = [u"ATTENDANCE"]

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        level = 0
        section = 0
        school = 0
        levels_by_sections = []
        attendance_students = []
        attendance_status = {}
        students = []
        date_format = '%Y-%m-%d'
        date_format_display = '%A %d/%m/%Y'

        # if has_group(self.request.user, 'SCHOOL') or has_group(self.request.user, 'DIRECTOR'):
        if self.request.user.school:
            school = self.request.user.school

        current_date = datetime.datetime.now().strftime(date_format)
        selected_date = self.request.GET.get('date', current_date)
        selected_date_view = datetime.datetime.strptime(selected_date, date_format).strftime(date_format_display)

        try:
            attendance = Attendance.objects.get(
                school_id=school.id,
                attendance_date=selected_date
                # attendance_date=datetime.datetime.strptime(selected_date, date_format)
            )
        except Attendance.DoesNotExist:
            attendance = ''

        if self.request.GET.get('level', 0):
            level = ClassRoom.objects.get(id=int(self.request.GET.get('level', 0)))
        if self.request.GET.get('section', 0):
            section = Section.objects.get(id=int(self.request.GET.get('section', 0)))

        education_year = EducationYear.objects.get(current_year=True)
        queryset = Enrollment.objects.filter(school_id=school, education_year=education_year)
        registrations = queryset.filter(
            classroom__isnull=False,
            section__isnull=False
        ).distinct().values(
            'classroom__name',
            'classroom_id',
            'section__name',
            'section_id'
        ).order_by('classroom_id')

        current_level_section = ''
        disable_attendance = False
        for registry in registrations:
            # disable_attendance = False
            exam_day = False
            school_closed = False
            validation_date = ''
            total_attended = 0
            total_absences = 0
            level_section = '{}-{}'.format(registry['classroom_id'], registry['section_id'])
            attendances = attendance.students[level_section] if attendance and attendance.students and level_section in attendance.students else ''
            total = queryset.filter(classroom_id=registry['classroom_id'], section_id=registry['section_id']).count()

            if attendances:
                total = attendances['total_enrolled']
                total_attended = attendances['total_attended']
                total_absences = attendances['total_absences']
                exam_day = attendances['exam_day']
                validation_date = attendance.validation_date
                school_closed = attendance.close_reason
                for value in attendances['students']:
                    attendance_status[value['student_id']] = value

            level_by_section = {
                'level_name': registry['classroom__name'],
                'level': registry['classroom_id'],
                'section_name': registry['section__name'],
                'section': registry['section_id'],
                'total': total,
                'total_attended': total_attended,
                'total_absences': total_absences,
                'exam_day': exam_day,
                'validation_date': validation_date,
                'disable_attendance': disable_attendance
            }

            if level and section and level.id == registry['classroom_id'] and section.id == registry['section_id']:
                current_level_section = level_by_section
                if exam_day or (attendance and attendance.validation_date) or school_closed:
                    disable_attendance = True

            levels_by_sections.append(level_by_section)

        if level and section:
            students = queryset.filter(classroom_id=level.id,section_id=section.id,
                                       # registration_date__lte=selected_date
                                      ).order_by('student__first_name')
            for line in students:
                student = line.student
                if str(student.id) in attendance_status:
                    student_status = attendance_status[str(student.id)]
                    line.attendance_status = student_status['status'] if 'status' in student_status else True
                    line.absence_reason = student_status['absence_reason'] if 'absence_reason' in student_status else ''
                    attendance_students.append(line)

        base = datetime.datetime.now()
        dates = []
        day_range = school.attendance_range if school.attendance_range else Attendance.DEFAULT_ATTENDANCE_RANGE

        for x in range(0, day_range):
            d = base - datetime.timedelta(days=x)
            dates.append({
                'value': d.strftime(date_format),
                'label': d.strftime(date_format_display)
            })

        return {
            'attendance': attendance,
            'disable_attendance': disable_attendance,
            'current_level_section': current_level_section,
            'total': queryset.count(),
            'total_students': students.count() if students else 0,
            'students': students,
            'school': school,
            'level': level,
            'section': section,
            'dates': dates,
            'classrooms': ClassRoom.objects.all(),
            'sections': Section.objects.all(),
            'levels_by_sections': levels_by_sections,
            'selected_date': selected_date,
            'selected_date_view': selected_date_view,
        }


class AbsenteeView(ListAPIView):
    """
    API endpoint for validated absentees
    """
    queryset = Absentee.objects.filter(
        school__location=True
    )
    serializer_class = AbsenteeSerializer
    permission_classes = (permissions.IsAdminUser,)
