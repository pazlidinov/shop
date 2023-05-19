from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
