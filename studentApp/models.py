from django.db import models

from studentApp.choices import MONTH_CHOICES


class DateAware(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Student(DateAware):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.IntegerField(choices=MONTH_CHOICES)
    dob = models.DateField()
    cell_phone_number = models.IntegerField(unique=True)
    home_phone_number = models.IntegerField()

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
