from django.shortcuts import render

def calc(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        op = request.POST['operation']
        if op == 'add':
            result = num1 + num2
        elif op == 'subtract':
            result = num1 - num2
        elif op == 'multiply':
            result = num1 * num2
        elif op == 'divide':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero!'
    return render(request, 'calculator/calc.html', {'res': result})
