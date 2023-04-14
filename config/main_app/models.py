from django.db import models

# Create your models here.


class Product_img(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    img = models.ForeignKey(
        Product_img, on_delete=models.CASCADE, related_name='imgs')
    count = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    description = models.TextField()
    added_date = models.DateField(auto_now_add=True)
    size = models.ForeignKey(
        Size, on_delete=models.PROTECT, related_name='sizes')
    color = models.ForeignKey(
        Color, on_delete=models.PROTECT, related_name='colors')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='categories')

    def __str__(self):
        return self.name
