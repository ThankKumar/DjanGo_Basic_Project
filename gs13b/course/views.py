from django.shortcuts import render

# Create your views here.
def leran_django(request):
    return render(request, 'course/courseone.html',
    #{'nm':True} #hello true
    #{'nm':'Django'} #hello django
    #bkank
    {'nm':'Djanog','st':5}
        )
