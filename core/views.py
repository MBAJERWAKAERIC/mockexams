from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')  # Render home.html in templates/

