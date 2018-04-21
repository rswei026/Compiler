__author__ = 'achamseddine'

from django.core.management.base import BaseCommand

from student_registration.enrollments.tasks import track_student_program_moves


class Command(BaseCommand):
    help = 'Track enrolled students programme moves'

    def handle(self, *args, **options):
        track_student_program_moves()
