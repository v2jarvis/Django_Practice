#all over the textutils config 
from django.http import HttpResponse
from  django.shortcuts import render

def val(request):
    return render(request,"index.html")

def analyze(request):
    text=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    fullsmall=request.GET.get('fullsmall','off')
    newlnrem=request.GET.get('newlnrem','off')

    #remove punctuation
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    if (removepunc=='on'):
        analyzed=''
        for i in text:
            if i not in punctuations:
                analyzed=analyzed+i
        val={'purpose':'removed punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',val)
    #lower to upper
    elif(fullcaps=='on'):
        analyzed=''
        for i in text:
            analyzed=analyzed+i.upper()
        val={'purpose':'Upppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',val)    
    #upper to lower
    elif(fullsmall=='on'):
        analyzed=''
        for i in text:
            analyzed=analyzed+i.lower()
        val={'purpose':'Lowercase','analyzed_text':analyzed}
        return render(request,'analyze.html',val)    
    #new line remover
    elif(newlnrem=='on'):
        analyzed=''
        for i in text:
            if i!='\n':
                analyzed=analyzed+i
        val={'purpose':'Newlineremove','analyzed_text':analyzed}
        return render(request,'analyze.html',val)            

    else:
        return HttpResponse("Error")