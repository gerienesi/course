import json
import os
from django.core.management.base import BaseCommand

from studentApp.models import Student

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Command(BaseCommand):
    help = 'Synchronize database Student model with items from sync-students.json'

    def handle(self, *args, **options):
        try:
            with open(os.path.join(BASE_DIR, '../students.json')) as config_file:
                config = json.load(config_file)

            Student.objects.all().delete()

            students = []

            for data in config:
                students.append(Student(first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        gender=data['gender'],
                                        dob=data['dob'],
                                        cell_phone_number=data['cell_phone_number'],
                                        home_phone_number=data['home_phone_number']))

            Student.objects.bulk_create(
                students
            )

            self.stdout.write(self.style.SUCCESS('Students synchronized successfully.'))

        except Exception as error:
            self.stdout.write(self.style.ERROR(error))
