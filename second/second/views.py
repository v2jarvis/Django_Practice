# this is views for seting configuration
from django.http import HttpResponse
from  django.shortcuts import render
def val(request):
    return render(request,"index.html")
def analyze(request):
    text=request.GET.get('text','default')
    #removepunc=request.GET.get('removepunc','off')
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

    analyzed=''
    for i in text:
        if i not in punctuations:
            analyzed=analyzed+i

    val={'purpose':'removed punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html',val)
