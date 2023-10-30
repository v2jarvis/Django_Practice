#all views here
from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    if request.method=='POST':
        one=request.POST['num1']
        two=request.POST['num2']
        return HttpResponse(int(one)+int(two))
    else:
        return render(request,'index.html')
