from django.shortcuts import render,redirect
from .forms import crudform
from .models import info

def myshow(request):
    show=info.objects.all()
    return render(request,'show.html',{'show':show})

def add(request):
    if request.method=='POST':
        data=crudform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('show')
    myobj=crudform()
    return render(request,'add.html',{'add':myobj})

def delete(request, id):
    data=info.objects.get(id=id)
    data.delete()
    return redirect('show')

def edit(request, id):
    instance=info.objects.get(id=id)
    if request.method == 'POST':
        form=crudform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('show')
    myobj=crudform(instance=instance)
        
    return render(request, 'edit.html', {'form': myobj})