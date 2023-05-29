import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import *
from .utils import check_article_view

# Create your views here.


def homePageView(request):
    return render(request, 'index.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

    def my_def(request, pk):
        product = Product.objects.get(pk=pk)
        if check_article_view(request, pk):
            product.update_view()
        else:
            pass
        return render(request, 'detail.html')


def create_comment(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        comment = request.POST.get("comment")
        u = None
        if request.user.is_authenticated:
            u = request.user
        else:
            u = None

        if len(comment) > 3:
            Comment.objects.create(product=product, user=u, comment=comment)

    return redirect("home:detail", id)


def delete_comment(request, comment_id):
    com = Comment.objects.get(pk=comment_id)
    com.delete()
    return redirect("home:detail", com.product.id)


def add_rating(request):

    data = json.loads(request.GET.get("data"))
    u = None
    if request.user.is_authenticated:
        u = request.user
    else:
        u = None

    if data:
        product = Product.objects.get(pk=int(data.get("product_id")))
        for rate in product.rating.all():
            print(rate.user)
            if request.user == rate.user:
                return JsonResponse({"status": 400})
        else:
            Rating.objects.create(
                value=int(data.get("rating")),
                product=product,
                user=u
            )
            return JsonResponse({"status": 200, "updated_rating": product.average_rating})
    else:
        return JsonResponse({"status": 404})


def sort_products(request):
    all_products = Product.objects.all()
    data = {
        'all_products': all_products,
    }
    return render(request, 'sort_products.html', context=data)


def sort_key_products(request, key_word):
    # lis = key_word.split(' ')
    lis = key_word.split('*')

    nam = lis[0]
    # cat = lis[1].split('+')
    col = lis[1].split('+')
    siz = lis[2].split('+')
    # cat.remove('')
    col.remove('')
    siz.remove('')

    if nam != '' or nam != ' ':
        p = Product.objects.filter(name__icontains=nam).order_by('-id')
    else:
        p = Product.objects.all().order_by('-id')
    # if len(cat) > 0:
    #     p.filter(category__in=cat)
    if len(col) > 0:
        p = p.filter(color__in=col)
    if len(siz) > 0:
        p = p.filter(size__in=siz)

    data = {
        'all_products': p,
    }
    return render(request, 'sort_products.html', context=data)


def sort_by_category(request, id):
    cat = Category.objects.get(id=id)
    p = Product.objects.filter(category=cat)
    data = {
        'all_products': p,
    }
    return render(request, 'sort_products.html', context=data)
