from .models import Category, Product
from cart.models import LikedCart, CardProduct

def main_context(request):
    categories = Category.objects.all() 
    liked_count=LikedCart.objects.filter(id=request.session['user_liked_id'])
    cart_count=CardProduct.objects.filter(products=request.session.get('user_cart_id'))
    data = {
        'category': categories,  
        'liked_count':liked_count,
        'cart_count':cart_count,
    }
    return data
