from .models import Category, Product, Color, Size
from cart.models import LikedCart, CardProduct


def main_context(request):
    all_categories = Category.objects.all()
    all_colors = Color.objects.all()
    all_sizes = Size.objects.all()

    data = {
        'all_categories': all_categories,
        'all_colors': all_colors,
        'all_sizes': all_sizes,
    }
    return data
