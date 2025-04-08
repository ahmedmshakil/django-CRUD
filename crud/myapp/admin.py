from django.contrib import admin
from .models import Student
from .models import FoodMenu
from .models import FoodMenuForm
# Register your models here.
admin.site.register(Student)
admin.site.register(FoodMenu)
admin.site.register(FoodMenuItem)