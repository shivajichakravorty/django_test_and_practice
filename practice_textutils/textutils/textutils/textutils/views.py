from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path


def index(request):
  return HttpResponse("Hello, World! <a " "href = https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7> Django Tutorial for Beginners </a>")

def about(request):
  return HttpResponse("This is the about page.")

def contact(request):
  filepath = Path(__file__).resolve().parent / '1.txt'
  with open(filepath, 'r') as file:
    content = file.read()
  return HttpResponse(content)