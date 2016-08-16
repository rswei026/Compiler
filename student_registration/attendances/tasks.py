__author__ = 'jcranwellward'

import datetime
import json
import os
from datetime import datetime

import requests
from django.conf import settings
from django.db import connection
from requests.auth import HTTPBasicAuth
from student_registration.taskapp.celery import app


def set_docs(docs):

    payload_json = json.dumps(
        {
            'docs': docs,
            'all_or_nothing': True
        }
    )
    path = os.path.join(settings.COUCHBASE_URL, '_bulk_docs')
    response = requests.post(
        path,
        headers={'content-type': 'application/json'},
        auth=HTTPBasicAuth(settings.COUCHBASE_USER, settings.COUCHBASE_PASS),
        data=payload_json,
    )
    return response


@app.task
def set_app_user(username, password):

    user_docs = []
    user_docs.append(
        {
            "_id": username,
            "type": "user",
            "username": username,
            "password": password,
            "organisation": username,
        }
    )

    response = set_docs(user_docs)
    return response.text


@app.task
def set_app_attendances():
    """
    Creates or edits a attendance document in Couchbase
    """
    docs = []
    from student_registration.students.models import ClassRoom
    from student_registration.alp.models import Registration
    from student_registration.attendances.models import Attendance
    classes = ClassRoom.objects.all()
    for item in classes:
        students = []
        attstudent = {}
        attendances = {}
        registrations = Registration.objects.filter(classroom_id=item.id, school_id=item.school.id)
        for reg in registrations:
            student = {
                "student_id": str(reg.student.id),
                "student_name": reg.student.full_name,
                "gender": reg.student.sex,
            }
            attstudent[str(reg.student.id)] = False
            students.append(student)

        attendqueryset = Attendance.objects.filter(classroom_id=item.id, school_id=item.school.id)
        for att in attendqueryset:
            attendances = {
                att.attendance_date.strftime('%d-%m-%Y'): {
                    "validation_date": att.validation_date.strftime('%d-%m-%Y'),
                    "students": attstudent
                }
            }
            attendances[att.attendance_date.strftime('%d-%m-%Y')]["students"][str(att.student.id)] = att.status

        doc = {
            "class_id": str(item.id),
            "class_name": item.name,
            "grade_id": str(item.grade.id),
            "grade_name": item.grade.name,
            "location_id": str(item.school.location.id),
            "location_name": item.school.location.name,
            "location_pcode": item.school.location.p_code,
            "school": str(item.school.id),
            "school_id": item.school.number,
            "school_name": item.school.name,
            "section_id": str(item.section.id),
            "section_name": item.section.name,
            "students": students,
            "attendance": attendances
        }
        docs.append(doc)

    response = set_docs(docs)
    if response.status_code in [requests.codes.ok, requests.codes.created]:
        return response.text


@app.task
def import_docs(**kwargs):
    """
    Imports docs from couch base
    """
    from student_registration.attendances.models import Attendance

    data = requests.get(
        os.path.join(settings.COUCHBASE_URL, '_all_docs?include_docs=true'),
        auth=HTTPBasicAuth(settings.COUCHBASE_USER, settings.COUCHBASE_PASS)
    ).json()

    for row in data['rows']:
        if 'attendance' in row['doc']:
            classroom = row['doc']['class_id']
            school = row['doc']['school']
            attendances = row['doc']['attendance']
            for key in attendances.keys():
                attendance = attendances[key]
                students = attendance['students']
                validation_date = ''
                if 'validation_date' in attendance:
                    validation_date = attendance['validation_date']
                attendance_date = key

                try:
                    validation_date = datetime.strptime(validation_date, '%d-%m-%Y').strftime('%Y-%m-%d')
                except Exception as exp:
                    pass
                try:
                    attendance_date = datetime.strptime(attendance_date, '%d-%m-%Y').strftime('%Y-%m-%d')
                except Exception as exp:
                    pass

                try:
                    for student_id in students.keys():
                        status = students[student_id]
                        instance = Attendance.objects.get(
                            student_id=student_id,
                            classroom_id=classroom,
                            school_id=school,
                            attendance_date=attendance_date
                        )
                    instance.status = status
                    if validation_date:
                        instance.validation_date = validation_date
                        instance.validation_status = True
                    instance.save()
                except Attendance.DoesNotExist:
                    instance = Attendance.objects.create(
                            student_id=student_id,
                            classroom_id=classroom,
                            school_id=school,
                            attendance_date=attendance_date,
                            status=status,
                    )
                    if validation_date:
                        instance.validation_date = validation_date
                        instance.validation_status = True
                    instance.save()
                except Exception as exp:
                    print exp.message
