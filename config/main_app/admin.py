from django.contrib import admin
from django.utils.html import mark_safe

from .models import *

# Register your models here.


@admin.register(Product_img)
class Product_imgAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'image']
    # list_editable = ['image']
    # list_display_links = ['image']
    list_per_page = 10
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Rating)
admin.site.register(Comment)