from django.db import models

# Create your models here.




class Size(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    img=models.ImageField()
    count = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    description = models.TextField()
    added_date = models.DateField(auto_now_add=True)
    size = models.ManyToManyField(Size, related_name='sizes')
    color = models.ManyToManyField(Color, related_name='colors')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='categories')

    def __str__(self):
        return self.name


class Product_img(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_img')
    slug = models.SlugField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name