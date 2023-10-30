#all views here
from django.shortcuts import render
from django.http import HttpResponse

def dis(request):
    return HttpResponse("helloo this is simple calculator")
def read(request):
    return render(request,'index.html')