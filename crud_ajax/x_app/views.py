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
    data=list(Student.objects.filter(user__startwith=val).values())
    print(data)
    return JsonResponse(data,safe=False)

def delete1(request):
    id=request.GET['id']
    data=Student.objects.get(id=id)
    data.delete()
    return JsonResponse({'message':'1'})

def edit(request):
    id=request.GET['id']
    data=list(Student.objects.filter(id=id).values())
    return JsonResponse(data,safe=False)

# def update(request):
#     print("-----------------start")
#     id=request.GET["id"]
#     name=request.GET["name"]
#     email=request.GET["email"]
#     course=request.GET["course"]
#     mobile=request.GET["mobile"]
#     address=request.GET["address"]
#     Student.objects.filter(id=id).update(name=name,email=email,course=course,mobile=mobile,address=address)
#     return JsonResponse({'message': '1'})

def update(request):
    print("-------------------start")
    if request.method == 'GET':
        # Get the parameters from the request
        id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        course = request.GET.get('course', None)
        mobile = request.GET.get('mobile', None)
        address = request.GET.get('address', None)

        # Check if mobile is empty or not a number
        if mobile is None or not mobile.isdigit():
            return JsonResponse({'error': 'Mobile number is missing or invalid.'}, status=400)

        # Convert mobile to integer
        mobile = int(mobile)

        # Update the record in the database
        Student.objects.filter(id=id).update(name=name, email=email, course=course, mobile=mobile, address=address)

        return JsonResponse({'message': '1'})

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)