from django.shortcuts import render

from .models import Category

# Create your views here.


def homePageView(request):    
    return render(request, 'index.html')


def detailPageView(request):
    return render(request, 'detail.html')
