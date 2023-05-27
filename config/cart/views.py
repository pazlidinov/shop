from django.shortcuts import render, redirect
from django.views.generic.base import View

# Create your views here.
from main_app.models import Product
from .models import Cart, CardProduct, LikedCart


def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()  # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return cart


def liked_cart_init(request):
    try:
        liked = LikedCart.objects.get(id=request.session.get('user_liked_id'))
    except:
        liked = LikedCart.objects.create()  # yangi cart object hosil qilish
        request.session['user_liked_id'] = liked.id
    return liked


class CartView(View):

    def get(self, request):
        cart = cart_init(request)

        return render(request, 'cart.html', {"cart": cart})


def AddToCartView(request, product_id):
    cart = cart_init(request)
    if cart.add(request, product_id):
        # cart.add(product_id)
        return redirect('/cart/')
    return render(request, 'cart.html', {"cart": cart})


def cart_remove(request, id):
    cart = cart_init(request)
    cart.remove_cart(id)
    # cart.product.filter(id=id).delete()
    return redirect('/cart/')


def cart_item_update(request):
    cart = cart_init(request)

    obj_id = int(request.GET.get('object_id'))
    qty = request.GET.get("quantity")

    cart.update_item(obj_id, qty)
    return redirect('/cart/')


def cart_delete(request):
    cart = cart_init(request)
    cart.clear_cart()
    return redirect('/cart/')


class LikedView(View):

    def get(self, request):
        liked = liked_cart_init(request)

        return render(request, 'liked.html', {"liked": liked})


class AddToLikedView(View):

    def get(self, request, product_id):
        liked = liked_cart_init(request)
        if liked:
            liked.add(product_id)
            return redirect('/cart/liked/')

        return render(request, 'liked.html', {"liked": liked})


def liked_remove(request, id):
    liked = liked_cart_init(request)
    liked.remove_likes(id)
    return redirect('/cart/liked/')
