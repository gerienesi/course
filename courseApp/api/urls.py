from django.urls import path
from courseApp import views as course_view

urlpatterns = [
    path('', course_view.CourseListCreateAPIView.as_view(), name='api-course-list'),
    path('<int:pk>/', course_view.PostDetailsAPIView.as_view(), name='api-course-details'),
]
