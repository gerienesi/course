from django.urls import path
from studentApp import views as student_view

urlpatterns = [
    path('', student_view.StudentListCreateAPIView.as_view(), name='api-student-list'),
    path('<int:pk>/', student_view.StudentDetailsAPIView.as_view(), name='api-student-details'),
]
