from django.shortcuts import render

# Create your views here.

def teacher_login(request):
    return render(request, 'teacher/login.html')

def teacher_signup(request):
    return render(request, 'teacher/signup.html')
