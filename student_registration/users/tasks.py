__author__ = 'achamseddine'

from student_registration.taskapp.celery import app


@app.task
def generate_passwords(group):
    from student_registration.users.models import User

    users = User.objects.filter(is_staff=False, is_superuser=False, groups__name=group)
    for user in users:
        try:
            password = user.username
            # if user.phone_number:
            #     password = password+user.phone_number[:2]
            if user.email:
                password = password+user.email[:2]
            user.update_password(password)
            user.save()
        except Exception as ex:
            print ex
            pass


@app.task
def assign_groups_to_2nd_shift_schools():
    from student_registration.users.models import User

    users = User.objects.filter(first_name='school')
    for user in users:
        try:
            for group in (1, 4, 8):
                user.groups.add(group)
                user.save()
        except Exception as ex:
            print ex
            pass


@app.task
def assign_groups_to_2nd_shift_directors():
    from student_registration.users.models import User

    users = User.objects.filter(first_name='director')
    for user in users:
        try:
            for group in (1, 4, 9):
                user.groups.add(group)
                user.save()
        except Exception as ex:
            print ex
            pass
