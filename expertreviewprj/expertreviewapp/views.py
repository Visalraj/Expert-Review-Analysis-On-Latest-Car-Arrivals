from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages

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

        return render(request,'demoregister.html') 

def login(request):
        if request.POST :
                email = request.POST['username']
                password = request.POST['password']
                user = authenticate(username = email,password = password)
                if user is None:
                        print("not found")
                else:
                        s=User.objects.get(email=email)
                        if s.email =="admin@gmail.com":
                                return redirect("/admin_dashboard")  
                        else:
                                
                                if user.is_staff==1:
                                         ex = Expert.objects.get(email = s.email)
                                         request.session['exid'] = ex.id
                                         request.session['exname'] = ex.firstname
                                         return redirect("/experthome")
                                else:
                                        d=Registration.objects.get(email=s.email)
                                        request.session['id']=d.id
                                        request.session['name']=d.firstname
                                        return redirect("/userhome")

                                                      
        return render(request,'login.html')

   

def about(request):
        return render(request,'aboutpage.html')
def admin(request):
        return render(request,'adminhome.html')
def viewuser(request):
        s = Registration.objects.all()
        return render(request,'viewuser.html',{"s":s})

def userhome(request):
        name=request.session['name']
        return render(request,'userhome.html',{"name":name})

def userprofile(request):
        id = request.session['id']
        b  = Registration.objects.get(id = id)
        if request.POST:
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                addone = request.POST['addone']
                addtwo  = request.POST['addtwo']
                email = request.POST['email']
                phone = request.POST['phone']
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                Registration.objects.filter(id=id).update(firstname = firstname,lastname = lastname,addressone = addone,addresstwo = addtwo, email = email,mobileno = phone,password = password,c_password = cpassword)
                messages.success(request,'Profile Updated Successfully.')
                return redirect("/userprofile")
        return render(request,'viewuserprofile.html',{"value":b})


def expertregistration(request):
        if request.POST :
                fname = request.POST['fname']
                lname = request.POST['lastname']
                gender = request.POST['gender']
                email = request.POST['email']
                mobno = request.POST['mobileno']
                experience = request.POST['exp']
                password = request.POST['password']
                con_password = request.POST['cpass']
                print(fname,lname,gender,email,mobno,experience,password,con_password)
                r = Expert.objects.create(firstname = fname,lastname = lname,gender = gender,email = email,mobilenumber = mobno,experience = experience,password = password,confirm_password = con_password )
                r.save()
                u = User.objects.create_user(username=email,password=password,is_superuser=0,is_active=0,is_staff = 1 ,email=email) 
                u.save()
        return render(request,'expertregistration.html')

def experthome(request):
        ename = request.session['exname']
        return render(request,'experthome.html',{"exname":ename})

def expertprofile(request):
        id = request.session['exid']
        val = Expert.objects.get(id = id)
        if request.POST:
                fname = request.POST['fname']
                lname = request.POST['lastname']
                email = request.POST['email']
                mob = request.POST['mobileno']
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                Expert.objects.filter(id = id).update(firstname = fname,lastname = lname,email = email,mobilenumber = mob,password = password,confirm_password = cpassword)
                messages.success(request, 'Profile updated successfully!')
                return redirect('/expertprofile')
              
        return render(request,'expertprofile.html',{"val":val})

def addcars(request):
        if request.POST:
                brandn = request.POST['brandname']
                carn =request.POST['carname']
                modeln = request.POST['modelname']
                seat = request.POST['seat']
                fuel = request.POST['fuel']
                price = request.POST['price']
                image = request.FILES['image']
                q = Car.objects.create(brandname = brandn,carname = carn,modelname=modeln,seats = seat,fuel = fuel,price = price,image = image)
                q.save()

        return render(request,'addcars.html')

def addreview(request):
        var = Car.objects.filter(rv=0)
        return render(request,'addreview.html',{"obj":var})


def viewexperts(request):
        obj = Expert.objects.all()
        return render(request,'viewexpert.html',{"value":obj})

def requestedexperts(request):
        s=User.objects.filter(is_staff=1,is_active=0).values_list('email')
        obj = Expert.objects.filter(email__in=s)
        return render(request,'requestedexperts.html',{"value":obj})


def expertreviews(request):
        obj = Expert.objects.all()
        return render(request,'expertreviews.html',{"value":obj})

def expertreviewoncar(request):
        exid = request.session['exid']
        crid = request.GET.get('id')
        expid=Expert.objects.get(id=exid)
        carid=Car.objects.get(id=crid)
        carimage = request.GET.get('image')
        if request.POST:
                # carid = request.POST['carid']
                mileage = request.POST['mileage']
                extandint = request.POST['ext']
                engandtrans = request.POST['engine']
                suspension = request.POST['sus']
                electric  =request.POST['electrical']
                fluids = request.POST['fluids']
                tires = request.POST['tires']
                info = request.POST['info']
                qu = Review.objects.create(cid = carid ,mileage = mileage,extandint = extandint,engine = engandtrans,suspension = suspension,electronics = electric,fluids = fluids,tires = tires,info = info,exp = expid )
                qu.save()
             
        return render(request,'expertreviewoncar.html',{"carid":carid,"image":carimage})

def expertreviewstatus(request):
    expid = request.session['exid']
    value = Review.objects.filter(exp=expid)
    return render(request, 'expertreviewstatus.html', {"values": value})

def showreviews(request):
        #get expert id from expert review
        expid = request.GET.get('id')
        value = Review.objects.filter(exp = expid,statusofreview = 0)
        return render(request,'showreviews.html',{"values":value})

def acceptreview(request):
        carid = request.GET.get('carid')
        Review.objects.filter(cid = carid).update(statusofreview=1)
        Car.objects.filter(id = carid).update(rv=1)
        return render(request,'acceptreview.html')


def carreviewbyexperts(request):
        car = Car.objects.filter(rv= 1)
        return render(request,'carreviewsbyexperts.html',{"value":car})



def managecars(request):
        val = Car.objects.all()
        return render(request,'managecars.html',{"value":val})


def viewreviewbyuser(request):
        id = request.GET.get('id')
        review = Review.objects.filter(cid = id)
        return render(request,'viewreviewbyuser.html',{"review":review})


def updatecardetails(request):
        id = request.GET.get('id')
        car = Car.objects.filter(id = id)
        if request.POST:
                bname = request.POST['brandname']
                cname = request.POST['carname']
                mname = request.POST['modelname']
                seats = request.POST['seat']
                fuel = request.POST['fuel']
                price = request.POST['price']
                Car.objects.filter(id = id).update(brandname = bname,carname = cname,modelname = mname,seats = seats,fuel = fuel,price = price)
                return redirect('/admin_dashboard')

        return render(request,'updatecardetails.html',{"cars":car})

def deletecars(request):
        id = request.GET.get('id')
        carobj = Car.objects.filter(id = id)
        carobj.delete()
        return render(request,'deletecars.html')

def deleteusers(request):
        id = request.GET.get('id')
        userobj = Registration.objects.filter(id = id)
        userobj.delete()
        return render(request,'deleteusers.html')

def activate(request):
        id=request.GET.get("id")
        r=Expert.objects.get(id=id)
        User.objects.filter(email=r.email).update(is_active=1)
        return redirect("/requestedexperts")

