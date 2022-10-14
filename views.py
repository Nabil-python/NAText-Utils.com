
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover   = request.POST.get('newlineremover', 'off')
    exteraspaceremover = request.POST.get('exteraspaceremover', 'off')
    CharacterCounter = request.POST.get('CharacterCounter', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':  'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
                
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(exteraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate (djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
            
                analyzed=analyzed+char
        params={'purpose': 'Extera Space Rmover', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(CharacterCounter=="on"):
        analyzed=('No. of characters given in the text are : '+str(len(djtext)))
        params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and exteraspaceremover!="on" and CharacterCounter!="on" ):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


