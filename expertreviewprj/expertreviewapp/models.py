from django.db import models

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


class Expert(models.Model):
    firstname = models.CharField(max_length=255,null=True)
    lastname = models.CharField(max_length=255,null=True)
    date = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=255,null=True)
    mobilenumber = models.CharField(max_length=20,null=True)
    experience = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=255,null=True)
    file = models.ImageField(null=True)
    status = models.BooleanField(default=False,null=True)


class Car(models.Model):
    brandname = models.CharField(max_length=255,null=True)
    carname = models.CharField(max_length=255,null=True)
    modelname = models.CharField(max_length=200,null=True)
    seats = models.CharField(max_length=255,null=True)
    fuel = models.CharField(max_length=20,null=True)
    price = models.CharField(max_length=200,null=True)
    image = models.ImageField()
    rv = models.CharField(max_length=200,null=True,default=0)


class Review(models.Model):
    cid = models.ForeignKey(Car,on_delete=models.CASCADE)
    mileage = models.CharField(max_length=255,null=True)
    extandint = models.CharField(max_length=200,null=True)
    engine = models.CharField(max_length=255,null=True)
    suspension = models.CharField(max_length=20,null=True)
    electronics = models.CharField(max_length=200,null=True)
    fluids = models.CharField(max_length=255,null=True)
    tires = models.CharField(max_length=255,null=True)
    info = models.CharField(max_length=200,null=True)
    exp = models.ForeignKey(Expert,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    statusofreview = models.IntegerField(default=0)

