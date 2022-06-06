from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns =[

    path('feesdj/', views.fees_django),
    path('feespy/', views.fees_python),
]