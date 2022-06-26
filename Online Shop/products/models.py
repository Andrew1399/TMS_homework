from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='products')

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
