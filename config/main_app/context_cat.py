from .models import Category, Product


def main_context(request):
    categories = Category.objects.all()
    all_products=Product.objects.all()
    data = {
        'category': categories,
        'all_products': all_products,
    }
    return data
