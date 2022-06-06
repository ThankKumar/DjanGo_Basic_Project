from django.shortcuts import render

from  django.http import HttpResponse
# Create your views here.
def fees_django(request):
    return HttpResponse("<h2>300</h2>")
def fees_python(request):
    return HttpResponse("<h2>400</h2>") 
