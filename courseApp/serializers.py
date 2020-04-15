from abc import ABC

from rest_framework import serializers

from courseApp.models import Course
from studentApp.models import Student
from studentApp.serializers import StudentSerializer

"""Course serializer

    1. To create a new course fields name, description are required
    
    2. To add existing student/students to the current course
        a. Raw Data
            Enter students id separated by comma(,) in `students_ids` field.
        b. HTML form
            Select student/students from `Students ids`
            
    3. To remove student/students from current course
        a. Raw Data
            Remove  students id in `students_ids` field.
        b. HTML form
            Unselect student/students you want to remove from `Students ids`

"""


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    students_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Student.objects.all(),
                                                      source='students', required=False)

    class Meta:
        model = Course
        depth = 1
        fields = ('pk', 'name', 'description', 'students', 'students_ids')
