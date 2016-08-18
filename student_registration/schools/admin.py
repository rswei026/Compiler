# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import (
    School,
    Course,
    EducationLevel,
    ClassLevel,
    Grade,
    Section,
    ClassRoom,
    PartnerOrganization,
)


admin.site.register(School)
# admin.site.register(Course)
admin.site.register(EducationLevel)
admin.site.register(ClassLevel)
admin.site.register(Grade)
admin.site.register(Section)
admin.site.register(ClassRoom)
admin.site.register(PartnerOrganization)

