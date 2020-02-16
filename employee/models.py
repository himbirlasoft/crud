from django.db import models

# Create your models here.
class Employee(models.Model):  
    name = models.CharField(max_length=100)  
    pan_number = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField()  
    city = models.CharField(max_length=20)  
    class Meta:  
        db_table = "employee"  