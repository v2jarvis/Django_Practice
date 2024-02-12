from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee

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

def show(request):
    data=Employee.objects.all()
    return render(request,'show.html',{'data':data})      
    
def del_data(request,sid):
    data=Employee.objects.get(sid=sid)
    data.delete()
    return redirect("show")
    
def edit(request,sid):
    data=Employee.objects.get(sid=sid)
    return render(request, 'edit.html', {'data': data})

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

