from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

def student_signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('student_signup')

        Student.objects.create(full_name=full_name, email=email, password=password)
        messages.success(request, 'Signup successful! You can now log in.')
        return redirect('student_login')

    return render(request, 'students/signup.html')


def student_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            student = Student.objects.get(email=email, password=password)
            return render(request, 'students/dashboard.html', {'student': student})
        except Student.DoesNotExist:
            messages.error(request, 'Invalid login credentials')
            return redirect('student_login')

    return render(request, 'students/login.html')
