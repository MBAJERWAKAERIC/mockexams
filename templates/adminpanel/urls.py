from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('signup/', views.admin_signup, name='admin_signup'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
