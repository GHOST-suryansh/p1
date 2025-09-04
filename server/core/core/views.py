from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  # core/templates/core/home.html banana hoga
