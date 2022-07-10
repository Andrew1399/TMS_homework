from django.core.cache import cache
from django.db.models import F, Sum
from shop.models import CartItem, Product, Order, OrderItem, Cart


class CartService:

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

    def get_total_price(self):
        # cart = Cart.objects.annotate(
        #     price=Sum(F('cartitem__product__price') * F('cartitem__quantity'))
        # ).get(
        #     order_user=request.user
        # )
        # cart.total = cart.price
        # cart.save()
        pass


class OrderService:

    def __init__(self, user):
        self.user = user
        self.cart_service = CartService(user)

    def create_order(self, user):
        order = Order.objects.create(
            user=user,
            total_price=self.cart_service.get_total_price()
        )
        return order

    def create_order_products(self, order):
        cart = self.cart_service.get_user_cart()

        order_items = OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                product=Product.objects.get(id=i['id']),
                qty=i['qty'],
            ) for i in cart['products']
        ])

        order.total_price = self.cart_service.get_total_price()
        order.save()

        return order_items
