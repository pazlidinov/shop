from django.contrib import admin
from .models import CardProduct, Cart, LikedCart
# Register your models here.


admin.site.register(CardProduct)
admin.site.register(Cart)
admin.site.register(LikedCart)

