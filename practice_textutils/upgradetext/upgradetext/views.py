

from django.http import HttpResponse
from urllib3 import HTTPResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Home")
    return render(request, 'index.html')

def removepunc(request):
    return HttpResponse("Remove Punctuation")

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Character Count")
