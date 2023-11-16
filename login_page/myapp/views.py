# Create your views here.
#import lib
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def register(request):
    if request.method=='POST':
        first=request.POST['first']
        last=request.POST['last']
        user=request.POST['user']
        email=request.POST['email']
        cpass=request.POST['cpass']
        rpass=request.POST['rpass']
        super=request.POST['super']
        staff=request.POST['staff']

        if(cpass==rpass):
            msg=User.objects.filter(username=user).exists()
            if(msg):
                print("Already Exist")
                return redirect('register')
            else:
                User.objects.create(first_name=first,last_name=last,username=user,email=email,password=make_password(rpass),is_superuser=super,is_staff=staff)
                return redirect('login')
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    else:
        return render(request,'register.html') 

def loginn(request):
    if request.method=='POST':
        user=request.POST['user']
        password=request.POST['password']
        user=authenticate(username=user,password=password)
        if(user is not None):
            login(request, user)
            return render(request,'user.html', {'user': user})
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    return render(request,'login.html')            

def logoutt(request):
    logout 
    return redirect('login')