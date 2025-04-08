from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodMenu
# Create your views here.
def home(request):
    items = FoodMenu.objects.all()
    return render(request, 'myapp/home.html', {'items': items})
    # return HttpResponse("Hello, django from myapp/ home views.....!")
    
    