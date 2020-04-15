from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courseApp.models import Course
from studentApp.models import Student


class CourseListCreateAPIView(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('api-course-list')

    def test_create_course(self):
        data = {
            'name': 'title',
            'description': 'text',
        }

        self.assertEquals(
            Course.objects.count(),
            0
        )

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Course.objects.count(),
            1
        )
        course = Course.objects.first()
        self.assertEquals(
            course.name,
            data['name']
        )

    def test_get_course_list(self):
        data = {
            'name': 'title',
            'description': 'text',
            'student': {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'johndoe@university.edu',
                'gender': 0,
                'dob': '1994-02-25',
                'cell_phone_number': 123456789,
                'home_phone_number': 123456789
            }

        }

        student = Student.objects.create(
            first_name=data['student']['first_name'],
            last_name=data['student']['last_name'],
            email=data['student']['email'],
            gender=data['student']['gender'],
            dob=data['student']['dob'],
            cell_phone_number=data['student']['cell_phone_number'],
            home_phone_number=data['student']['home_phone_number'],
        )

        course = Course.objects.create(name=data['name'], description=data['description'])
        course.students.add(student)

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['name'],
            course.name
        )
        self.assertEquals(
            data['description'],
            course.description
        )
        self.assertEquals(
            data['students'][0]['first_name'],
            student.first_name
        )


class CourseDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.course = Course(name='Course title', description='Course description')
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@university.edu',
            gender=0,
            dob='1994-02-25',
            cell_phone_number=123456789,
            home_phone_number=12345678,
        )
        self.course.save()
        self.course.students.add(self.student)
        self.url = reverse('api-course-details', kwargs={'pk': self.course.pk})

    def test_get_course_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            self.course.pk
        )
        self.assertEquals(
            data['name'],
            self.course.name
        )
        self.assertEquals(
            data['description'],
            self.course.description
        )

    def test_update_course(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['name'] = 'Course new title'
        data['description'] = 'Course new description'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.course.refresh_from_db()
        self.assertEquals(
            self.course.name,
            data['name']
        )
        self.assertEquals(
            self.course.description,
            data['description']
        )

    def test_delete_course(self):
        self.assertEquals(
            Course.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Course.objects.count(),
            0
        )

    def test_add_student_to_course(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()

        st = {
            'first_name': 'John_new',
            'last_name': 'Doe_new',
            'email': 'johndoe@university.edu.al',
            'gender': 0,
            'dob': '1994-02-25',
            'cell_phone_number': 123456781,
            'home_phone_number': 1234567812
        }

        student = Student.objects.create(
            first_name=st['first_name'],
            last_name=st['last_name'],
            email=st['email'],
            gender=st['gender'],
            dob=st['dob'],
            cell_phone_number=st['cell_phone_number'],
            home_phone_number=st['home_phone_number'],
        )
        current_students = list(self.course.students.values_list('id', flat=True))
        current_students.append(student.pk)
        data['students_ids'] = current_students

        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.course.refresh_from_db()
        self.assertEquals(
            self.course.students.all().count(),
            2
        )
        self.assertEquals(
            self.course.students.last().first_name,
            st['first_name']
        )

    def test_remove_student_from_course(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()

        current_students = list(self.course.students.values_list('id', flat=True))

        data['students_ids'] = []
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(current_students),
            1
        )

        current_students = list(self.course.students.values_list('id', flat=True))
        self.assertEquals(
            len(current_students),
            0
        )
