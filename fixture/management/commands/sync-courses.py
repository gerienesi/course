import json
import os
from django.core.management.base import BaseCommand

from courseApp.models import Course
from studentApp.models import Student

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Command(BaseCommand):
    help = 'Synchronize database Course model with items from sync-courses.json'

    def handle(self, *args, **options):
        try:
            with open(os.path.join(BASE_DIR, '../courses.json')) as config_file:
                config = json.load(config_file)

            Course.objects.all().delete()

            courses = []

            for data in config:
                courses.append(Course(name=data['name'], description=data['description']))

            Course.objects.bulk_create(
                courses
            )

            self.stdout.write(self.style.SUCCESS('Courses synchronized successfully.'))

        except Exception as error:
            self.stdout.write(self.style.ERROR(error))
