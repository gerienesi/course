from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from courseApp.models import Course
from courseApp.serializers import CourseSerializer


class CourseListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of courses or create new
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete course
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
