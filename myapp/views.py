from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from django.http import JsonResponse    

def home(request):
    return HttpResponse("This is home page")

def data(request):
    data = {
        "name": "John Doe",
        "age": 25,
        "city": "New York"
    }
    return JsonResponse(data)

# def even_odd(request, number):
def even_odd(request):
    number = 47
    if number % 2 == 0:
        return HttpResponse(f"{number} is even")
    else:
        return HttpResponse(f"{number} is odd")
    
    
def htmlfile(request):  
        return render(request, 'index.html')


def datafile(request):
    a = "Django is a framework"
    return render(request, 'index.html', {'data': a})


def home(request):
    return HttpResponse("This is home page")


def help(request):
    return HttpResponse("This is help page")


def name(request,name):
    return HttpResponse(f"My name is : {name}")

def number(request, number):
    return HttpResponse(f"The number is: {number}")


def string(request, string):
    return HttpResponse(f"The string is: {string}")


def even_odd(request, num):
    if num % 2 == 0:
        return HttpResponse(f"{num} is even")
    else:
        return HttpResponse(f"{num} is odd")


def Jsondata(request):
    data = {
        'name': "Anand Yadav",
        'course': "Django",
        'Fees': 5000,
    }
    return JsonResponse(data)


def Jsondata2(request):
    data = {
        'name': "Anand Yadav",
        'course': ["Django", "Java", "C++", "C"],
        'Address': "Jalandhar",
    }
    return JsonResponse(data)


def Jsondata3(request):
    data = {
        'user1': {
            'name' : "Anand Yadav",
            'course' : "Django",
        },
        'user2': {
            'name': "Sourabh Kumar",
            'course': "Python",
        }
    }
    return JsonResponse(data)


def display(request, username):
    return HttpResponse(f"My name is {username}")


def year(request, year):
    return HttpResponse(f"The year is {year}")


def uservalue(request, username):
    return HttpResponse(f"User value is: {username}")


def website(request, data):
    try:
        result = 10 / data
        return HttpResponse(f"Result: {result}")
    except ZeroDivisionError:
        return HttpResponse("Division by zero is not allowed")
    
def handler404(request,exception):
    return HttpResponse("Page not found")


def base(request):
    return render(request, "base.html")


def form(request):
    return render(request, "form.html")

def galaxy(request):
    return render(request, "galaryPage.html")