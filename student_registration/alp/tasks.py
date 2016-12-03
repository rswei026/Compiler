__author__ = 'achamseddine'

import json
import os

from datetime import datetime
from student_registration.taskapp.celery import app


@app.task
def assign_alp_level():
    from student_registration.alp.models import Outreach
    from student_registration.schools.models import EducationLevel

    records = Outreach.objects.all()
    for record in records:
        try:
            level = record.level
            to_level = 0
            if not level:
                continue
            if level.id == 1 or level.id == 2 or level.id == 3:
                total = record.exam_total
                if total <= 40:
                    to_level = 1
                elif total > 40 and total <= 80:
                    to_level = 2
                elif total > 80 and total <= 120:
                    to_level = 3

            if level.id == 4 or level.id == 5 or level == 6:
                total = record.exam_total
                if total <= 20:
                    to_level = 1
                elif total > 20 and total <= 40:
                    to_level = 2
                elif total > 40 and total <= 60:
                    to_level = 3
                elif total > 60 and total <= 100:
                    to_level = 4
                elif total > 100 and total <= 140:
                    to_level = 5
                elif total > 140 and total <= 180:
                    to_level = 6

            if level.id == 7 or level.id == 8 or level.id == 9:
                total = record.exam_total
                if total <= 20:
                    to_level = 1
                elif total > 20 and total <= 40:
                    to_level = 2
                elif total > 40 and total <= 60:
                    to_level = 3
                elif total > 60 and total <= 80:
                    to_level = 4
                elif total > 80 and total <= 100:
                    to_level = 5
                elif total > 100 and total <= 120:
                    to_level = 6
                elif total > 120 and total <= 160:
                    to_level = 7
                elif total > 160 and total <= 200:
                    to_level = 8
                elif total > 200 and total <= 240:
                    to_level = 9

            if to_level:
                print level.id, total, to_level
                record.assigned_to_level = EducationLevel.objects.get(id=to_level)
                record.save()
        except Exception as ex:
            print ex.message
            continue