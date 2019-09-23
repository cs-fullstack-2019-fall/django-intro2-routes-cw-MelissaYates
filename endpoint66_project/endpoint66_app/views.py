from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request, userinput):
    return HttpResponse(userinput)
def goGetTheGood(request):
    return HttpResponse("Here you go!")
def happyHappyJoyJoy(request):
    return HttpResponse("Going to the beach")
def endPoint(request):
    return HttpResponse("Hello!")