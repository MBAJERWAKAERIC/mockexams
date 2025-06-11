from django.db import models
from students.models import Student
from subjects.models import Subject

# Stores raw marks for a student in a subject
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    raw_score = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 87.50

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.raw_score}"
