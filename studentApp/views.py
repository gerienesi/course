from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from studentApp.models import Student
from studentApp.serializers import StudentSerializer


class StudentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of students or create new
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete student
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
