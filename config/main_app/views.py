from django.shortcuts import redirect, render
from django.views.generic import DetailView

from .models import *
from .utils import check_article_view

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

    def my_def(request, pk):
        article = Product.objects.filter(pk=pk).first()
        if check_article_view(request, pk):
            article.view += 1
            article.save()
        else:
            pass
       