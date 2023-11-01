from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee
def std_info(request):
    if(request.method=='POST'):
        name=request.POST['name']
        mobile=request.POST['mob']
        email=request.POST['email']

        Employee.objects.create(name=name,mobile=mobile,email=email)
        return redirect('show')
    else:
        return render(request,'index.html')

def show(request):
    data=Employee.objects.all()
    return render(request,'show.html',{'data':data})