from django.contrib import admin
from django.urls import path, include  # include is needed here

from core import views  # adjust based on where your home view is

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('student/', include('students.urls')),
    path('teacher/', include('teachers.urls')),
    path('adminpanel/', include('adminpanel.urls')),  # <--- NO slash at the beginning
]
