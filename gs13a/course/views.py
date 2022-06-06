from django.shortcuts import render
''' date time ke liye datetime import karna parta hai gs13c 
from datetime import datetime '''
# Create your views here.
'''
13a
def learn_django(request):
    cname='Django'
    duration='6\Month'
    seats=10
    django_details = {'nm':cname,'du':duration, 'st':seats}
    return render(request,'course/courseone.html', django_details)
'''
   # context=
    
#    {'nm':'Django'}

'''13b
'''
'''13c

def learn_django(request):
    return render(request,'course/courseone.html',
    {'nm':'django is god of all Devloper'
    
    })
    '''
'''datertime ke liye'''
'''
gs13c
def learn_django(request):
    d = datetime.now()
    return render(request,'course/courseone.html',
    {'dt':d})
    '''
def learn_django(request):
    return render(request, 'course/courseone.html',
        {'p1':56.123456, 'p2':56.000000, 'p3':56.012365
    
        })
