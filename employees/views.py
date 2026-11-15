
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Employee Management Portal!")


def about(request):
    return HttpResponse("About Us: This portal manages employee information.")


def greet(request, name):
    return HttpResponse(f"Hello, {name}! Welcome to the Employee Portal.")
