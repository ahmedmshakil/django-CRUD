from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    # address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.age} - {self.city}"
    
class FoodMenu(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200) 
    price = models.IntegerField()
    image = models.URLField(max_length=60000000000)

    def __str__(self):
        return f"{self.item_name} - {self.price} tk"