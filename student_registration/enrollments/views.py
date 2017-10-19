# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import ListView, FormView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.utils.translation import ugettext as _
from django.db.models import Q

import tablib
from rest_framework import status
from rest_framework import viewsets, mixins, permissions
from braces.views import GroupRequiredMixin, SuperuserRequiredMixin
from import_export.formats import base_formats

from student_registration.alp.templatetags.util_tags import has_group

from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin

from .filters import EnrollmentFilter
from .tables import BootstrapTable, EnrollmentTable

from student_registration.outreach.models import Child
from student_registration.outreach.serializers import ChildSerializer
from student_registration.schools.models import ClassRoom
from .models import Enrollment, EnrollmentGrading, LoggingStudentMove, EducationYear, LoggingProgramMove
from .forms import EnrollmentForm, GradingTermForm, GradingIncompleteForm, StudentMovedForm
from .serializers import EnrollmentSerializer, LoggingStudentMoveSerializer, LoggingProgramMoveSerializer
from student_registration.users.utils import force_default_language
from student_registration.backends.tasks import export_2ndshift, export_2ndshift_gradings


class AddView(LoginRequiredMixin,
              GroupRequiredMixin,
              FormView):

    template_name = 'bootstrap4/common_form.html'
    form_class = EnrollmentForm
    success_url = '/enrollments/list/'
    group_required = [u"ENROL_CREATE"]

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(AddView, self).get_context_data(**kwargs)

    def get_initial(self):
        initial = super(AddView, self).get_initial()
        data = {
            'new_registry': self.request.GET.get('new_registry', '0'),
            'student_outreached': self.request.GET.get('student_outreached', '1'),
            'have_barcode': self.request.GET.get('have_barcode', '1')
        }
        if self.request.GET.get('enrollment_id'):
            instance = Enrollment.objects.get(id=self.request.GET.get('enrollment_id'))
            data = EnrollmentSerializer(instance).data
            data['student_nationality'] = data['student_nationality_id']
            data['student_mother_nationality'] = data['student_mother_nationality_id']
            data['student_id_type'] = data['student_id_type_id']
        if self.request.GET.get('child_id'):
            instance = Child.objects.get(id=int(self.request.GET.get('child_id')))
            data = ChildSerializer(instance).data
        initial = data

        return initial

    # def get_form(self, form_class=None):
    #     if self.request.method == "POST":
    #         return EnrollmentForm(self.request.POST, request=self.request)
    #     else:
    #         return EnrollmentForm(self.get_initial())

    def form_valid(self, form):
        form.save(self.request)
        return super(AddView, self).form_valid(form)


class EditView(LoginRequiredMixin,
               GroupRequiredMixin,
               FormView):

    template_name = 'bootstrap4/common_form.html'
    form_class = EnrollmentForm
    success_url = '/enrollments/list/'
    group_required = [u"ENROL_EDIT"]

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(EditView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Enrollment.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return EnrollmentForm(self.request.POST, instance=instance)
        else:
            data = EnrollmentSerializer(instance).data
            data['student_nationality'] = data['student_nationality_id']
            data['student_mother_nationality'] = data['student_mother_nationality_id']
            data['student_id_type'] = data['student_id_type_id']
            return EnrollmentForm(data, instance=instance)

    def form_valid(self, form):
        instance = Enrollment.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(EditView, self).form_valid(form)


class MovedView(LoginRequiredMixin,
                GroupRequiredMixin,
                FormView):

    template_name = 'enrollments/moved.html'
    form_class = StudentMovedForm
    success_url = '/enrollments/list/'
    group_required = [u"SCHOOL"]

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(MovedView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        instance = Enrollment.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return StudentMovedForm(self.request.POST, instance=instance, moved=self.kwargs['moved'])
        else:
            return StudentMovedForm(instance=instance, moved=self.kwargs['moved'])

    def form_valid(self, form):
        instance = Enrollment.objects.get(id=self.kwargs['pk'])
        moved = LoggingStudentMove.objects.get(id=self.kwargs['moved'])
        moved.school_to = self.request.user.school
        moved.save()
        form.save(request=self.request, instance=instance)
        return super(MovedView, self).form_valid(form)


class ListingView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FilterView,
                  ExportMixin,
                  SingleTableView,
                  RequestConfig):

    table_class = EnrollmentTable
    model = Enrollment
    template_name = 'enrollments/list.html'
    table = BootstrapTable(Enrollment.objects.all(), order_by='id')
    filterset_class = EnrollmentFilter
    group_required = [u"SCHOOL"]

    def get_queryset(self):
        force_default_language(self.request)
        education_year = EducationYear.objects.get(current_year=True)
        return Enrollment.objects.exclude(moved=True).filter(
            education_year=education_year,
            school=self.request.user.school_id
        )


class GradingView(LoginRequiredMixin,
                  GroupRequiredMixin,
                  FormView):

    template_name = 'enrollments/grading.html'
    form_class = GradingTermForm
    success_url = '/enrollments/list/'
    group_required = [u"ENROL_GRADING"]

    def get_context_data(self, **kwargs):
        force_default_language(self.request)
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(GradingView, self).get_context_data(**kwargs)

    def get_form_class(self):
        if int(self.kwargs['term']) == 4:
            return GradingIncompleteForm
        return GradingTermForm

    def get_form(self, form_class=None):
        form_class = self.get_form_class()
        instance = EnrollmentGrading.objects.get(id=self.kwargs['pk'])
        if self.request.method == "POST":
            return form_class(self.request.POST, instance=instance)
        else:
            return form_class(instance=instance)

    def form_valid(self, form):
        instance = EnrollmentGrading.objects.get(id=self.kwargs['pk'])
        form.save(request=self.request, instance=instance)
        return super(GradingView, self).form_valid(form)


####################### API VIEWS #############################


class LoggingProgramMoveViewSet(mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):

    model = LoggingProgramMove
    queryset = LoggingProgramMove.objects.all()
    serializer_class = LoggingProgramMoveSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LoggingStudentMoveViewSet(mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):

    model = LoggingStudentMove
    queryset = LoggingStudentMove.objects.all()
    serializer_class = LoggingStudentMoveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.method in ["PATCH", "POST", "PUT"]:
            return self.queryset
        terms = self.request.GET.get('term', 0)
        current_year = EducationYear.objects.get(current_year=True)
        if terms:
            qs = self.queryset.filter(
                school_to__isnull=True,
                education_year=current_year
            ).exclude(enrolment__dropout_status=True)
            for term in terms.split():
                qs = qs.filter(
                    Q(student__first_name__contains=term) |
                    Q(student__father_name__contains=term) |
                    Q(student__last_name__contains=term) |
                    Q(student__id_number__contains=term)
                )
            return qs
        return self.queryset

    def post(self, request, *args, **kwargs):
        if request.POST.get('moved', 0):
            enrollment = Enrollment.objects.get(id=request.POST.get('moved', 0))
            current_year = EducationYear.objects.get(current_year=True)
            enrollment.moved = True
            enrollment.save()
            LoggingStudentMove.objects.get_or_create(
                enrolment_id=enrollment.id,
                student_id=enrollment.student_id,
                school_from_id=enrollment.school_id,
                education_year=current_year
            )
        return JsonResponse({'status': status.HTTP_200_OK})


class EnrollmentViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """
    Provides API operations around a Enrollment record
    """
    model = Enrollment
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.GET.get('moved', 0):
            return self.queryset
        if self.request.method in ["PATCH", "POST", "PUT"]:
            return self.queryset
        if self.request.user.school_id:
            return self.queryset.filter(school_id=self.request.user.school_id).order_by('classroom_id', 'section_id')

        return self.queryset

    def delete(self, request, *args, **kwargs):
        instance = self.model.objects.get(id=kwargs['pk'])
        instance.delete()
        return JsonResponse({'status': status.HTTP_200_OK})

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()

    def partial_update(self, request, *args, **kwargs):
        if request.POST.get('moved', 0):
            moved = LoggingStudentMove.objects.get(id=request.POST.get('moved', 0))
            moved.school_to_id = request.POST.get('school')
            moved.save()
            enrollment = moved.enrolment
            enrollment.moved = False
            enrollment.save()
        self.serializer_class = EnrollmentSerializer
        return super(EnrollmentViewSet, self).partial_update(request)


class ExportViewSet(LoginRequiredMixin, ListView):

    model = Enrollment
    queryset = Enrollment.objects.all()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.queryset.filter(owner=self.request.user)
        return self.queryset

    def get(self, request, *args, **kwargs):
        data = ''
        school = request.GET.get('school', 0)

        if self.request.user.school_id:
            school = self.request.user.school_id
        if school:
            data = export_2ndshift({'current': 'true', 'school': school})

        response = HttpResponse(
            data,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename=registration_list.xlsx'
        return response


class ExportGradingViewSet(LoginRequiredMixin, ListView):

    model = EnrollmentGrading
    queryset = EnrollmentGrading.objects.all()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.queryset.filter(owner=self.request.user)
        return self.queryset

    def get(self, request, *args, **kwargs):
        data= ''
        school = request.GET.get('school', 0)

        if self.request.user.school_id:
            school = self.request.user.school_id
        if school:
            data = export_2ndshift_gradings({'current': 'true', 'school': school})

        response = HttpResponse(
            data,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename=registration_list.xlsx'
        return response


class ExportBySchoolView(LoginRequiredMixin, ListView):

    model = Enrollment
    queryset = Enrollment.objects.all()

    def get(self, request, *args, **kwargs):

        schools = self.queryset.values_list(
                        'school', 'school__number', 'school__name', 'school__location__name',
                        'school__location__parent__name', 'school__number_students_2nd_shift', ).distinct().order_by('school__number')

        data = tablib.Dataset()
        data.headers = [
            _('CERD'),
            _('School name'),
            _('# Students registered in the Compiler'),
            _('# Students reported by the Director'),
            _('District'),
            _('Governorate'),
        ]

        content = []
        for school in schools:
            nbr = self.model.objects.filter(school=school[0]).count()
            content = [
                school[1],
                school[2],
                nbr,
                school[5],
                school[3],
                school[4]
            ]
            data.append(content)

        file_format = base_formats.XLS()
        response = HttpResponse(
            file_format.export_data(data),
            content_type='application/vnd.ms-excel',
        )
        response['Content-Disposition'] = 'attachment; filename=student_by_school.xls'
        return response


class ExportByCycleView(LoginRequiredMixin, ListView):

    model = Enrollment
    queryset = Enrollment.objects.all()

    def get(self, request, *args, **kwargs):

        classrooms = ClassRoom.objects.all()
        schools = self.queryset.values_list(
                        'school', 'school__number', 'school__name', 'school__location__name',
                        'school__location__parent__name', ).distinct().order_by('school__number')

        data = tablib.Dataset()
        data.headers = [
            _('CERD'),
            _('School name'),
            _('# Students registered in the Compiler'),
            'Class name',
            '# Students registered in class',
            _('District'),
            _('Governorate'),
        ]

        content = []
        for school in schools:
            enrollments = self.model.objects.filter(school=school[0])
            nbr = enrollments.count()
            for cls in classrooms:
                nbr_cls = enrollments.filter(classroom=cls).count()
                if not nbr_cls:
                    pass

                content = [
                    school[1],
                    school[2],
                    nbr,
                    cls.name,
                    nbr_cls,
                    school[3],
                    school[4]
                ]
                data.append(content)

        file_format = base_formats.XLS()
        response = HttpResponse(
            file_format.export_data(data),
            content_type='application/vnd.ms-excel',
        )
        response['Content-Disposition'] = 'attachment; filename=student_by_cycle.xls'
        return response
