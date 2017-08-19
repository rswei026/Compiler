from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import ArrayField, JSONField

from model_utils import Choices
from model_utils.models import TimeStampedModel

from student_registration.students.models import Student, Labour
from student_registration.locations.models import Location
from student_registration.schools.models import (
    School,
    ClassRoom,
    EducationalLevel,
)


class Assessment(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    overview = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    assessment_form = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Cycle(models.Model):

    name = models.CharField(max_length=100)
    current_cycle = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class RSCycle(models.Model):

    name = models.CharField(max_length=100)
    current_cycle = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Site(models.Model):

    name = models.CharField(max_length=100)
    current_cycle = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Referral(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Disability(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class CLM(TimeStampedModel):

    LANGUAGES = Choices(
        ('english_arabic', _('English/Arabic')),
        ('french_arabic', _('French/Arabic'))
    )
    STATUS = Choices(
        'enrolled',
        'pre_test',
        'post_test'
    )

    district = models.ForeignKey(
        Location,
        blank=True, null=True,
        related_name='+',
    )
    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    language = ArrayField(
        models.CharField(
            choices=LANGUAGES,
            max_length=50,
            blank=True,
            null=True,
        ),
        blank=True,
        null=True,
    )
    student = models.ForeignKey(
        Student,
        blank=False, null=True,
        related_name='clm_enrollments',
    )
    disability = models.ForeignKey(
        Disability,
        blank=True, null=True,
        related_name='+',
    )
    have_labour = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=Choices((1, _("Yes")), (0, _("No")))
    )
    labours = ArrayField(
        models.ForeignKey(
            Labour,
            blank=True, null=True,
            related_name='+',
        ),
        blank=True,
        null=True,
    )
    labour_hours = models.IntegerField(
        max_length=5,
        blank=True,
        null=True,
    )
    hh_educational_level = models.ForeignKey(
        EducationalLevel,
        blank=True, null=True,
        related_name='+',
    )

    status = models.CharField(max_length=50, choices=STATUS, default=STATUS.enrolled)
    pre_test = JSONField(blank=True, null=True)
    post_test = JSONField(blank=True, null=True)

    scores = JSONField(blank=True, null=True, default=dict)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False, null=True,
        related_name='+',
    )
    deleted = models.BooleanField(blank=True, default=False)
    dropout_status = models.BooleanField(blank=True, default=False)
    moved = models.BooleanField(blank=True, default=False)
    outreach_barcode = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    new_registry = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=Choices((1, _("Yes")), (0, _("No")))
    )
    student_outreached = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=Choices((1, _("Yes")), (0, _("No")))
    )
    have_barcode = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=Choices((1, _("Yes")), (0, _("No")))
    )
    registration_date = models.DateField(
        blank=True,
        null=True,
    )

    @property
    def student_fullname(self):
        if self.student:
            return self.student.full_name
        return ''

    @property
    def student_age(self):
        if self.student:
            return self.student.age
        return 0

    def get_absolute_url(self):
        return '/clm/edit/%d/' % self.pk

    def __unicode__(self):
        if self.student:
            return self.student.__unicode__()
        return str(self.id)

    class Meta:
        abstract = True


class BLN(CLM):

    cycle = models.ForeignKey(
        Cycle,
        blank=True, null=True,
        related_name='+',
    )
    referral = ArrayField(
        models.ForeignKey(
            Cycle,
            blank=True, null=True,
            related_name='+',
        ),
        blank=True,
        null=True,
    )


class RS(CLM):

    SCHOOL_SHIFT = Choices(
        ('first', _('First shift')),
        ('second', _('Second shift')),
    )

    cycle = models.ForeignKey(
        RSCycle,
        blank=True, null=True,
        related_name='+',
    )
    site = models.ForeignKey(
        Site,
        blank=True, null=True,
        related_name='+',
    )
    school = models.ForeignKey(
        School,
        blank=False, null=True,
        related_name='+',
    )
    shift = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=SCHOOL_SHIFT
    )


class CBECE(CLM):

    MUAC = Choices(
        ('1', _('< 11.5 CM (severe malnutrition)')),
        ('2', _('< 12.5 CM (moderate malnutrition)')),
    )

    cycle = models.ForeignKey(
        Cycle,
        blank=True, null=True,
        related_name='+',
    )
    site = models.ForeignKey(
        Site,
        blank=True, null=True,
        related_name='+',
    )
    school = models.ForeignKey(
        School,
        blank=False, null=True,
        related_name='+',
    )
    referral = ArrayField(
        models.ForeignKey(
            Cycle,
            blank=True, null=True,
            related_name='+',
        ),
        blank=True,
        null=True,
    )
    child_muac = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=MUAC
    )
    grade = models.ForeignKey(
        ClassRoom,
        blank=True, null=True,
        related_name='+',
    )
    referral_reasons = ArrayField(
        models.ForeignKey(
            Cycle,
            blank=True, null=True,
            related_name='+',
        ),
        blank=True,
        null=True,
    )
    pre_test_arabic = models.IntegerField(
        blank=True,
        null=True,
        choices=((x, x) for x in range(1, 20))
    )
    pre_test_language = models.FloatField(
        blank=True,
        null=True,
        choices=((x, x) for x in range(1, 20))
    )
    pre_test_math = models.FloatField(
        blank=True,
        null=True,
        choices=((x, x) for x in range(1, 20))
    )
    pre_test_science = models.FloatField(
        blank=True,
        null=True,
        choices=((x, x) for x in range(1, 20))
    )
    school_readiness = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
