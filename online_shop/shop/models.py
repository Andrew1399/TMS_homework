from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='products')
    available_inventory = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(blank=True, null=True)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title}: {self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        self.total_price = sum(item.get_cost() for item in self.products.all())
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ManyToManyField(Product, related_name='order_products')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = self.product.price
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.id)
