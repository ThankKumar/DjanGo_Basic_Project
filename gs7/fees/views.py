from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def fees_django(request):
    return HttpResponse(3000)
def fees_python(request):
    return HttpResponse(4000)