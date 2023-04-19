from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Registration (models.Model):
     firstname = models.CharField(max_length=50,null=True)
     lastname = models.CharField(max_length=50,null=True)
     dob = models.CharField(max_length=100,null=True)
     gender = models.CharField(max_length=50,null=True)
     addressone = models.CharField(max_length=250,null=True)
     addresstwo= models.CharField(max_length=250,null=True)
     state = models.CharField(max_length=250,null=True)
     district = models.CharField(max_length=250,null=True)
     city = models.CharField(max_length=250,null=True)
     pincode = models.CharField(max_length=250,null=True)
     mobileno = models.CharField(max_length=250,null=True)
     email = models.CharField(max_length=100,null=True)
     password = models.CharField(max_length=50,null=True)
     c_password = models.CharField(max_length=100,null=True) 
     role =  models.CharField(max_length=100,null=True)





class Cars(models.Model):
     Brand_Name = models.CharField(max_length=100,null=True)
     Car_Name = models.CharField(max_length=100,null=True)
     Model_Name = models.CharField(max_length=100,null=True)
     Seat = models.CharField(max_length=50,null=True)
     Fuel = models.CharField(max_length=100,null=True)
     Price = models.CharField(max_length=100,null=True)
     
     
     
     
