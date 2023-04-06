from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Product_img)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Sub_category)
