from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This is for the root URL
    
]
