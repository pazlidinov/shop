from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg

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
    img = models.ImageField()
    count = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    description = models.TextField()
    added_date = models.DateField(auto_now_add=True)
    size = models.ManyToManyField(Size, related_name='sizes')
    color = models.ManyToManyField(Color, related_name='colors')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='categories')

    @property
    def average_rating(self):
        rating = self.rating.all().aggregate(Avg('value'))['value__avg']
        if rating:
            return str(rating)
        else:
            return 0

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating')


class Product_img(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_img')
    image = models.ImageField()


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    comment = models.TextField()
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product.slug)
