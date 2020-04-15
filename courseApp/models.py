from django.db import models

from studentApp.models import Student


class DateAware(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Course(DateAware):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return "{0} {1}".format(self.name, self.description)
