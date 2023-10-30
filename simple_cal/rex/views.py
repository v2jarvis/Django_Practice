#all views here
from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    if request.method=='POST':
        one=request.POST['num1']
        two=request.POST['num2']

        op=request.POST['op']
        result=0
        if (op=='+'):
            result=int(one)+int(two)
        elif (op=='-'):
            result=int(one)-int(two)
        elif (op=='*'):
            result=int(one)*int(two)
        elif (op=='/'):
            try:
                result=int(one)/int(two)
            except ZeroDivisionError:
                print('can not divide by zero')                
        
        return HttpResponse(result)
    else:
        return render(request,'index.html')
