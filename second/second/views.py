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
    spacerem=request.GET.get('spacerem','off')
    charcount=request.GET.get('charcount','off')

    #remove punctuation
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    if (removepunc=='on'):
        analyzed=''
        for i in text:
            if i not in punctuations:
                analyzed=analyzed+i
        val={'purpose':'PunctuationsRemoved','analyzed_text':analyzed}
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
        val={'purpose':'Newlineremoved','analyzed_text':analyzed}
        return render(request,'analyze.html',val)            
    
    #extraspaceremover
    elif(spacerem=='on'):
        analyzed=''
        for i in text:
            analyzed=analyzed+i.replace(" ","")
        val={'purpose':'SapceRemoved','analyzed_text':analyzed}
        return render(request,'analyze.html',val)                
    
    #charcount
    elif(charcount=='on'):
        analyzed=len(text)
        val={'purpose':'CharCounter','analyzed_text':analyzed}
        return render(request,'analyze.html',val)                
    
    else:
        return HttpResponse("Error")