from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index_view(request):

    return render(request, 'index.html')

def analyze(request):

    djtext=request.POST.get('text', 'default')

    #Checking check box condition off or on:
    text_simply=request.POST.get('text_simply', 'default')
    punc=request.POST.get('punc', 'default')
    upper=request.POST.get('upper', 'default')
    remove_newline=request.POST.get('remove_newline', 'default')
    space_remover=request.POST.get('space_remover', 'default')
    charcount=request.POST.get('charcount', 'default')

    #if text is on:
    if text_simply == "on":
        analyzed=""
        for char in djtext:
                analyzed=analyzed+char
        jay={'purpose':'Get text simply', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', jay)


    #if punc is on follow this:
    if punc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
                if char not in punctuations:
                    analyzed=analyzed+char
        jay={'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', jay)

    #if upper is on follw this
    if upper=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        jay={'purpose':'Changing to Upper Case', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', jay)

    # if newline is on follow  this
    if remove_newline == "on":
        analyzed=""
        for char in djtext:
            if djtext !='\n':
                analyzed=analyzed + char
        jay={'purpose':'Removing extra line', 'ex_line_remover':analyzed}
        return render(request, 'analyze.html', jay)

    #if space_remover is on follow  this:
    if space_remover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed + char
            #if djtext[index]==" " and djtext[index+1]==" ":
                #pass
            #else:
                #analyzed=analyzed+char
        jay={'purpose':'Removing extra line', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', jay)

    #if charcount is on follow this:
    if charcount == "on":
        analyzed=len(djtext)
        jay={'purpose':'Removing extra line', 'Number_of_characters':analyzed}
        return render(request, 'analyze.html', jay)

    else:
        return HttpResponse("error")