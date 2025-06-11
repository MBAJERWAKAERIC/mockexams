from django.db import models

# Represents a school registered for exams
class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# Represents an examining body like UNEB, WAEC, etc.
class ExamBody(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Represents a subject offered by a school
class Subject(models.Model):
    name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    exam_body = models.ForeignKey(ExamBody, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_code} - {self.name}"
