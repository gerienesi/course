from rest_framework import serializers

from studentApp.models import Student

"""Student serializer

    1. Required fields `first_name`, `last_name`, `email`, `gender`, `dob`, `cell_phone_number`, `home_phone_number`

"""


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'email', 'gender', 'dob', 'cell_phone_number', 'home_phone_number',)

