from django.shortcuts import render

# View to load homepage
def home(request):
    return render(request, 'home.html')
