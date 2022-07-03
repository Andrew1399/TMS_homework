from django.core.cache import cache

from shop.models import CartItem, Product


class CartService:
    '''Класс для работы с корзиной'''

    def __init__(self, user) -> None:
        self.user = user
        self.cart = self.get_user_cart()

    def add_product(self, product_data: dict):
        product: Product = Product.objects.get(id=product_data['product'])
        print('product', product)

        data_to_insert = {
            'title': product.title,
            'price': product.price,
            'quantity': product_data['quantity']
        }
        self.cart['products'].append(data_to_insert)

        cache.set(self.user.id, self.cart)

    def get_user_cart(self):
        cart = cache.get(self.user.id)
        return cart if cart else {'products': []}