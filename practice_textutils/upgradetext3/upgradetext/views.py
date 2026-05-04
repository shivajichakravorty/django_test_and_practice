

import string

from django.http import HttpResponse
from fastapi import params
from urllib3 import HTTPResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('fullcaps', 'off')
    newlineremove = request.GET.get('newlineremover', 'off')
    spaceremove = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    punctuation_list = list(string.punctuation)
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuation_list:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    elif uppercase == "on":
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    elif newlineremove == "on":
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    elif spaceremove == "on":
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        count = 0
        for char in djtext:
            if char != " ":
                count = count + 1
        analyzed = "Total Characters (without spaces) are: " + str(count)
        params = {'purpose': 'Counted Characters', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")











# def ex1(request):
#     params = {'name': 'Shivaji', 'place': 'India'}
#     return render(request, 'ex1.html', params)


# def removepunc(request):
#     return HttpResponse"Remove Punctuation")

# def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlineremove(request):
#     return HttpResponse("New Line Remove")

# def spaceremove(request):
#     return HttpResponse("Space Remove")

# def charcount(request):
#     return HttpResponse("Character Count")
