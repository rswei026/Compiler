# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import Http404
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, mixins, permissions
import tablib
from rest_framework import status
from django.utils.translation import ugettext as _
from import_export.formats import base_formats
from django.core.urlresolvers import reverse

from student_registration.students.models import (
    Person,
    Student,
    Nationality,
    IDType,
)
from student_registration.schools.models import (
    School,
    ClassRoom,
    Grade,
    Section,
)
from student_registration.students.serializers import StudentSerializer
from student_registration.registrations.forms import (
    RegisteringAdultForm,
    RegisteringChildForm,
)
from student_registration.students.forms import StudentForm
from student_registration.eav.models import (
    Attribute,
    Value,
)

from .models import Registration, RegisteringAdult
from .serializers import RegistrationSerializer, RegisteringAdultSerializer, RegistrationChildSerializer
from .utils import get_unhcr_principal_applicant


class RegistrationView(LoginRequiredMixin, ListView):
    """
    Provides the registration page with lookup types in the context
    """
    model = Registration
    template_name = 'registrations/list.html'

    def get_context_data(self, **kwargs):
        data = self.model.objects.all()
        if not self.request.user.is_staff:
            data = data.filter(owner=self.request.user)
            self.template_name = 'registrations/index.html'

        return {
            'registrations': data,
            'classrooms': ClassRoom.objects.all(),
            'schools': School.objects.all(),
            'grades': Grade.objects.all(),
            'sections': Section.objects.all(),
            'nationalities': Nationality.objects.all(),
            'genders': (u'Male', u'Female'),
            'months': Person.MONTHS,
            'idtypes': IDType.objects.all(),
            'columns': Attribute.objects.filter(type=Registration.EAV_TYPE),
            'eav_type': Registration.EAV_TYPE
        }

####################### API VIEWS #############################


class RegistrationViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    """
    Provides API operations around a registration record
    """
    model = Registration
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if not self.request.user.is_staff:
            if self.request.user.school:
                return self.queryset.filter(school=self.request.user.school.id)
            else:
                return []

        return self.queryset


class RegisteringAdultViewSet(mixins.RetrieveModelMixin,
                              mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):

    lookup_field = 'id_number'
    model = RegisteringAdult
    queryset = RegisteringAdult.objects.all()
    serializer_class = RegisteringAdultSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = super(RegisteringAdultViewSet, self).get_queryset()
        id_number = self.kwargs.get('id_number')
        if id_number:
            return queryset.filter(id_number=id_number)
        return queryset

    def get_object(self):
        """
        Try to lookup the registering adult from the UNHCR registration database
        :return:
        """
        try:
            adult = super(RegisteringAdultViewSet, self).get_object()
        except Http404:
            if self.kwargs.get('id_type'):
                principal_applicant = get_unhcr_principal_applicant(self.kwargs.get('id_number'))
                if principal_applicant:
                    adult = RegisteringAdult()
                    adult.id_number = principal_applicant["CaseNo"]
                    adult.phone = principal_applicant["CoAPhone"]
                    adult.first_name = principal_applicant["GivenName"]
                    adult.last_name = principal_applicant["FamilyName"]
                    adult.father_name = principal_applicant["FatherName"]
                    dob = principal_applicant["DOB"]
                    adult.birthday_day = dob.day
                    adult.birthday_month = dob.month
                    adult.birthday_year = dob.year
                    adult.sex = principal_applicant["Sex"]
                    adult.save()
                    return adult
            raise Http404
        else:
            return adult


class RegisteringChildViewSet(mixins.RetrieveModelMixin,
                              mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):

    model = Registration
    queryset = Registration.objects.all()
    serializer_class = RegistrationChildSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RegisteringPilotView(LoginRequiredMixin, FormView):
    template_name = 'registration-pilot/registry.html'
    model = RegisteringAdult

    def get_context_data(self, **kwargs):

        return {
            'form': RegisteringAdultForm({'location': self.request.user.location_id}),
            'student_form': StudentForm
        }

    def get_success_url(self):
        return reverse('registrations:registering_pilot')


class ExportViewSet(LoginRequiredMixin, ListView):
    model = Registration

    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.queryset.filter(owner=self.request.user)
        return self.queryset

    def get(self, request, *args, **kwargs):

        queryset = self.queryset
        data = tablib.Dataset()
        data.headers = [
            _('Student number'), _('Student fullname'), _('Mother fullname'), _('Nationality'),
            _('Day of birth'), _('Month of birth'), _('Year of birth'), _('Sex'),
            _('ID Number tooltip'), _('Phone number'), _('Student living address'),
            # _('Section'), _('Grade'),
            _('Class room'),
            _('School'), _('School number')
        ]

        content = []
        for line in queryset:
            # if not line.student or not line.grade or not line.section or not line.school:
            if not line.student or not line.classroom or not line.school:
                continue
            content = [
                '',
                line.student.full_name,
                line.student.mother_fullname,
                line.student.nationality.name,
                int(line.student.birthday_day),
                int(line.student.birthday_month),
                int(line.student.birthday_year),
                _(line.student.sex),
                line.student.id_number,
                line.student.phone,
                line.student.address,
                line.classroom.name,
                # line.section.name,
                # line.grade.name,
                line.school.name,
                line.school.number
            ]
            data.append(content)

        file_format = base_formats.XLS()
        response = HttpResponse(
            file_format.export_data(data),
            content_type='application/vnd.ms-excel',
        )
        response['Content-Disposition'] = 'attachment; filename=registration_list.xls'
        return response
