from .models import Category


def main_context(request):
    categories=Category.objects.all()
    context = {
        'category': categories
    }
    return context
