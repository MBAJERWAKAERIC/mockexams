from django.db import models
from subjects.models import School

# Represents a student registered for exams
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.registration_number} - {self.full_name}"
