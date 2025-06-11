from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import School, ExamBody, Subject

admin.site.register(School)
admin.site.register(ExamBody)
admin.site.register(Subject)
