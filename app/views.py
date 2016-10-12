from django.shortcuts import render

# Create your views here.


def func_add(number1, number2):
    return int(number1) + int(number2)


def func_sub(number1, number2):
    return int(number1) - int(number2)


def func_mult(number1, number2):
    return int(number1) * int(number2)


def func_div(number1, number2):
    return int(number1) / int(number2)


def index_view(request):
    if request.GET:
        number1 = request.GET["number1"]
        number2 = request.GET["number2"]
        functions = request.GET["functions"]
        if functions == "+":
            answer = func_add(number1, number2)
        if functions == "-":
            answer = func_sub(number1, number2)
        if functions == "*":
            answer = func_mult(number1, number2)
        if functions == "/":
            try:
                answer = func_div(number1, number2)
            except ZeroDivisionError:
                answer = 0

    else:
        answer = 0
        number1 = 0
        number2 = 0
        functions = 0

    context = {
        "answer": answer,
        "number1": number1,
        "number2": number2,
        "function": functions
    }
    return render(request, "index.html", context)
