from .models import Category, Product


def main_context(request):
    categories = Category.objects.all()   
    data = {
        'category': categories,        
    }
    return data
