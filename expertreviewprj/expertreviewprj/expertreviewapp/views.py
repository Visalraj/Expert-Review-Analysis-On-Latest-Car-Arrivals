from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your views here.

def home(request):
        return render(request,'index.html')


def common(request):
        return render(request,'commonheader.html')

   


def register(request):
        if request.POST :
                fname = request.POST['firstname']
                lname = request.POST['lastname']
                dob = request.POST['date']
                gender = request.POST['gender']
                addone = request.POST['addlineone']
                addtwo = request.POST['addlinetwo']
                state = request.POST['state']
                district = request.POST['district']
                city = request.POST['city']
                pincode = request.POST['pincode']
                mobile = request.POST['phone']
                email = request.POST['email']
                password = request.POST['password']
                c_password = request.POST['cpassword']

                
               
                r = Registration.objects.create(firstname = fname,lastname = lname,dob = dob,gender = gender,addressone = addone,addresstwo = addtwo,
                state = state,district = district,city = city,pincode = pincode,mobileno=mobile,email = email,
                password = password,c_password = c_password)
                r.save()
                u=User.objects.create_user(username=email,password=password,is_superuser=0,is_active=1,email=email)
                u.save()

        return render(request,'register.html')      

def login(request):
        if request.POST :
                email = request.POST['username']
                password = request.POST['password']
                user = authenticate(username = email,password = password)
                if user is None:
                        return redirect("/nosuchuser")
                else:
                        s=User.objects.get(email=email)
                        print(s)
                        if s.email=="admin@gmail.com":
                                return redirect("/admin_dashboard")
                        else:
                                return redirect("/user_dashboard")
                
                       
        
        
        return render(request,'login.html')

   

def about(request):
        return render(request,'aboutpage.html')

def contact(request):
        return render(request,'contact.html')
def admin(request):
        param_value = request.GET.get('param')
        context = {'param':param_value}
        return render(request,'adminhome.html',context)



def addcars(request):
        if request.POST:
                brandname = request.POST['brandname']
                carname = request.POST['carname']
                modelname = request.POST['modelname']
                seat = request.POST['seat']
                fuel = request.POST['fuel']
                price = request.POST['price']
                Car = Cars.objects.create(Brand_Name = brandname,Car_Name = carname,
                Model_Name = modelname,Seat = seat,Fuel = fuel,Price = price)
                Car.save()     
        return render(request,'addcars.html')


def managecars(request):
        return render(request,'managecars.html')

def manageusers(request):
        return render(request,'manageusers.html')

def manageexperts(request):
        return render(request,'manageexperts.html')

def queries(request):
        return render(request,'queries.html')


def userhome(request):
        return render(request,'userhome.html')

def nosuchuser(request):
        return render(request,'no_such_user.html')

def experthome(request):
        return render(request,'experthome.html')
