from .models import Employee
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

def home(request):
    return render(request,'home.html')


@login_required(login_url="/loginn")
def std_info(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mobile=request.POST['mob']
        email=request.POST['email']
        address=request.POST['address']
        course=request.POST['course']

        Employee.objects.create(name=name,mobile=mobile,email=email,address=address,course=course)
        return redirect('show')
    else:
        return render(request,'index.html')


@login_required(login_url="/loginn")
def show(request):
    data=Employee.objects.all()
    return render(request,'show.html',{'data':data})      
    
@login_required(login_url="/loginn")    
def del_data(request,sid):
    data=Employee.objects.get(sid=sid)
    data.delete()
    return redirect("show")

@login_required(login_url="/loginn")
def edit(request,sid):
    data=Employee.objects.get(sid=sid)
    return render(request, 'edit.html', {'data': data})

@login_required(login_url="/loginn")
def update(request, sid):
    if request.method=='POST':
        data=Employee.objects.get(sid=sid)
        data.name=request.POST['name']
        data.mobile=request.POST['mob']
        data.email=request.POST['email']
        data.address=request.POST['address']
        data.course=request.POST['course']
        data.save()
        return redirect('show')
    else:
        return redirect('show')
    

def register(request):
    if request.method=='POST':
        first=request.POST.get('first', '')
        last=request.POST.get('last', '')
        user=request.POST.get('user', '')
        email=request.POST.get('email', '')
        cpass=request.POST.get('cpass', '')
        rpass=request.POST.get('rpass', '')
        super=request.POST.get('super', False)
        staff=request.POST.get('staff', False)


        if(cpass==rpass):
            msg=User.objects.filter(username=user).exists()
            if(msg):
                print("Already Exist")
                return redirect('register')
            else:
                User.objects.create(first_name=first,last_name=last,username=user,email=email,password=make_password(rpass),is_superuser=super,is_staff=staff)
                return redirect('start')
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
            return redirect('start')
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    return render(request,'login.html')


def logoutt(request):
    logout(request)
    return redirect('start')