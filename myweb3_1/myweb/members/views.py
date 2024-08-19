from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def members(request):
    return HttpResponse("EEEE")

def profile(request):
    return HttpResponse("aaaaa")
    
def first(request):
  template = loader.get_template('myfirst.html')
  
  return HttpResponse(template.render())

def Second(request):
  template = loader.get_template('mySecond.html')
  
  return HttpResponse(template.render())

def Third(request):
  template = loader.get_template('myThird.html')
  
  return HttpResponse(template.render())