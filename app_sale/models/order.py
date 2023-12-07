from django.db import models as m

from app_sale.models.base import BaseEntity
from app_sale.models.product import Product


class Order(BaseEntity):
    full_name = m.CharField(max_length=70)
    phn_number = m.CharField(max_length=20)
    email = m.EmailField()
    address = m.CharField(max_length=120)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.items = None

    def __str__(self):
        return f'{self.id} {self.full_name}'

    def get_total_coast(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(BaseEntity):
    orderItem = m.ForeignKey(Order, related_name='items', on_delete=m.CASCADE)
    products = m.ForeignKey(Product, related_name='order_items', on_delete=m.CASCADE)
    price = m.DecimalField(max_digits=10, decimal_places=2)
    quantity = m.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
