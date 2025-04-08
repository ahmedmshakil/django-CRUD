
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home),
    path('additem/', views.additem, name='additem'),
   
]
