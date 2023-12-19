from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyModel
import json

def add(request):
    if request.method=='POST':
            # json_data=form.cleaned_data.get('json_data')
            # MyModel.objects.create(json_data=json_data)
            # csv_data=form.cleaned_data.get('csv_data')
            # MyModel.objects.create(csv_data=csv_data)

            # json_file=request.FILES.get('json_file')
            # csv_file=request.FILES.get('csv_file')

            # if json_file:
            #     json_data1=json.loads(json_file.read().decode('utf-8'))
            #     MyModel.objects.create(json_data=json_data1)
            # if csv_file:
            #     csv_data1=csv_file.read().decode('utf-8')
            #     MyModel.objects.create(csv_data=csv_data1)
                    
            return HttpResponse('success') 

    return render(request, 'add.html')

