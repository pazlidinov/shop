from django.shortcuts import render
from django.views.generic import DetailView

from .models import Category, Product, Product_img

# Create your views here.


def homePageView(request):
    return render(request, 'index.html')


# def detailPageView(request, id=1):
#     products=Product.objects.filter(id=id)
#     print(products)
#     # print(product)
#     data={
#         'product':products,
#     }
#     print(data)
#     return render(request, 'detail.html', context=data)


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
