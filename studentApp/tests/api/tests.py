from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from studentApp.models import Student


class StudentListCreateAPIView(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('api-student-list')

    def test_create_student(self):
        data = {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'johndoe@university.edu',
                'gender': 0,
                'dob': '1994-02-25',
                'cell_phone_number': 123456789,
                'home_phone_number': 123456789
            }

        self.assertEquals(
            Student.objects.count(),
            0
        )

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Student.objects.count(),
            1
        )
        student = Student.objects.first()
        self.assertEquals(
            student.first_name,
            data['first_name']
        )

    def test_get_student_list(self):
        data = {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'johndoe@university.edu',
                'gender': 0,
                'dob': datetime.strptime('25/02/1994', '%d/%m/%Y'),
                'cell_phone_number': 123456789,
                'home_phone_number': 123456789
            }

        student = Student.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            gender=data['gender'],
            dob=data['dob'],
            cell_phone_number=data['cell_phone_number'],
            home_phone_number=data['home_phone_number'],
        )

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
            data['first_name'],
            student.first_name
        )
        self.assertEquals(
            data['last_name'],
            student.last_name
        )
        self.assertEquals(
            data['email'],
            student.email
        )
        self.assertEquals(
            data['gender'],
            student.gender
        )
        self.assertEquals(
            datetime.strptime(data['dob'], '%Y-%m-%d'),
            student.dob
        )
        self.assertEquals(
            data['cell_phone_number'],
            student.cell_phone_number
        )
        self.assertEquals(
            data['home_phone_number'],
            student.home_phone_number
        )


class StudentDetailsAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@university.edu',
            gender=0,
            dob=datetime.strptime('25/02/1994', '%d/%m/%Y'),
            cell_phone_number=123456789,
            home_phone_number=12345678,
        )
        self.url = reverse('api-student-details', kwargs={'pk': self.student.pk})

    def test_get_student_details(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        self.assertEquals(
            data['pk'],
            self.student.pk
        )
        self.assertEquals(
            data['first_name'],
            self.student.first_name
        )
        self.assertEquals(
            data['last_name'],
            self.student.last_name
        )

    def test_update_student(self):
        response = self.client.get(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        data = response.json()
        data['first_name'] = 'John new'
        data['last_name'] = 'Doe new'
        response = self.client.put(self.url, data=data, format='json')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.student.refresh_from_db()
        self.assertEquals(
            self.student.first_name,
            data['first_name']
        )
        self.assertEquals(
            self.student.last_name,
            data['last_name']
        )

    def test_delete_student(self):
        self.assertEquals(
            Student.objects.count(),
            1
        )
        response = self.client.delete(self.url)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEquals(
            Student.objects.count(),
            0
        )
