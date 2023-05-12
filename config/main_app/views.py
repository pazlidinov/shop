import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView

from .models import *
from .utils import check_article_view

# Create your views here.


def homePageView(request):
    return render(request, 'index.html')


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


def create_comment(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        comment = request.POST.get("comment")
        u = None
        if request.user.is_authenticated:
            u = request.user
        else:
            u = None

        if len(comment) > 3:
            Comment.objects.create(product=product, user=u, comment=comment)

    return redirect("home:detail", pk)


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
