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


@admin.register(Product_img)
class Product_imgAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug": ('name',)}
