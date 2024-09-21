from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse

def create(request):
    if request.method=='POST':
        user=request.POST['user']
        password=request.POST['pass']
        email=request.POST['email']
        Student.objects.create(user=user,password=password,email=email)
        return HttpResponse("data saved")
    return render(request,'create.html')


def show(request):
    return render(request,'show.html')


def re(request):
    data=list(Student.objects.values())
    return JsonResponse(data,safe=False)


def insert(request):
    
        user = request.GET["user"]
        email = request.GET["email"]
        password = request.GET["password"]
        Student.objects.create(user=user,email=email,password=password)
        return JsonResponse({'message': '1'})

def search1(request):
    val=request.GET['search']
    data=list(Student.objects.filter(user__contains=val).values())
    print(data)
    return JsonResponse(data,safe=False)

def erase(request):
    print("reached")
    val=request.GET['id']
    data=Student.objects.get(id=val)
    data.delete()
    return JsonResponse({1:1})

def edit(request):
    val=request.GET['id']
    data=list(Student.objects.filter(id=val).values())
    
    return JsonResponse(data,safe=False)
     
    
def update(request):
        id=request.GET['id']
        user = request.GET["name"]
        email = request.GET["email"]
        Student.objects.filter(id=id).update(user=user,email=email,password=1234)
        return JsonResponse({'message': '1'})