from __future__ import unicode_literals, absolute_import, division

from django.utils.translation import ugettext as _
from django import forms
from student_registration.students.models import (
    Student
)
from student_registration.registrations.models import Registration


class StudentForm(forms.ModelForm):

    relation_to_adult = forms.ChoiceField(
                     choices=Registration.RELATION_TYPE, widget=forms.Select, required=False
                )
    enrolled_last_year = forms.ChoiceField(
                     choices=Registration.ENROLLMENT_TYPE, widget=forms.Select, required=False
                )

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = '__all__'
