from django.shortcuts import render

from .models import Category, Product

# Create your views here.


def homePageView(request):    
    return render(request, 'index.html')


def detailPageView(request):
    products=Product.objects.filter(id=1).values()
    # print(product)
    data={
        'product':products
    }
    print(data)
    return render(request, 'detail.html', context=data)
