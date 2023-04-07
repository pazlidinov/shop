from .models import Category


def main_context(request):
    categories = Category.objects.all()
    data = {
        'category': categories
    }
    return data
