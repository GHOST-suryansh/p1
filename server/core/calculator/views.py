from django.shortcuts import render

def calc(request):
    return render(request, 'calculator/calc.html') 
