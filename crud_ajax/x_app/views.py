from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def dashboard(request):
    return render(request,'dashboard.html')       

def insert(request):    
    name=request.GET['name']
    course=request.GET['course']
    mobile=request.GET['mobile']
    email=request.GET['email']
    address=request.GET['address']
    Student.objects.create(name=name,course=course,mobile=mobile,email=email,address=address)
    return JsonResponse({'message':'1'})

def re(request):
    data=list(Student.objects.values())
    return JsonResponse(data,safe=False)

def search1(request):
    val=request.GET['search']
    data=list(Student.objects.filter(user__contains=val).values())
    print(data)
    return JsonResponse(data,safe=False);