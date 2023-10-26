# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def dis(request):
    return HttpResponse("This is Simple Week Day Show using Key")

# weeks={
#     'mon':'Monday',
#     'tue':'Tuesday',
#     'wed':'Wednesday',
#     'thu':'Thursday',
#     'fri':'Friday',
#     'sat':'Saturday',
#     'sun':'Sunday'
# }
# def week(request,key):
#     return HttpResponse(f'<h1>{weeks[key]}</h1>')
    

