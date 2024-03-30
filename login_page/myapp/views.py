# Create your views here.
#import lib
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

def home(request):
    response=render(request,"home.html")
    response.set_cookie('homepage','homepagecookie', max_age=3600)
    return response

def about(request):
    response=render(request,"about.html")
    response.set_cookie('about','aboutcookie', max_age=3600)
    return response

@login_required(login_url="/login")
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
            
            return redirect('user')
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    return render(request,'login.html')            

@login_required(login_url="/login")
def user(request):
    return render(request,'user.html')

def logoutt(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login")
def analyze(request):
    if request.method=='POST':
        text = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        fullsmall = request.POST.get('fullsmall', 'off')
        newlnrem = request.POST.get('newlnrem', 'off')
        spacerem = request.POST.get('spacerem', 'off')
        charcount = request.POST.get('charcount', 'off')
    
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        if (removepunc=='on'):
            analyzed=''
            for i in text:
                if i not in punctuations:
                    analyzed=analyzed+i
            val={'purpose':'PunctuationsRemoved','analyzed_text':analyzed}
            return render(request,'analyze.html',val)

        elif(fullcaps=='on'):
            analyzed=''
            for i in text:
                analyzed=analyzed+i.upper()
            val={'purpose':'Upppercase','analyzed_text':analyzed}
            return render(request,'analyze.html',val)    

        elif(fullsmall=='on'):
            analyzed=''
            for i in text:
                analyzed=analyzed+i.lower()
            val={'purpose':'Lowercase','analyzed_text':analyzed}
            return render(request,'analyze.html',val)               

        elif(spacerem=='on'):
            analyzed=''
            for i in text:
                analyzed=analyzed+i.replace(" ","")
            val={'purpose':'SapceRemoved','analyzed_text':analyzed}
            return render(request,'analyze.html',val)                

        elif(charcount=='on'):
            analyzed=len(text)
            val={'purpose':'CharCounter','analyzed_text':analyzed}
            return render(request,'analyze.html',val)                
        
        else:
            return HttpResponse("Error")
    else:
        return render(request,'user.html')    