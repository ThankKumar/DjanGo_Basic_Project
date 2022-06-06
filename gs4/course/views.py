from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse('Home Page')
def learn_django(request):
    return HttpResponse('Hello Django')




# Create your views here.
