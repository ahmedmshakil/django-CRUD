from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, django from shakil.....!")

def info(request):
    return HttpResponse("This is a crud application, ABOUT INFO PAGE.")