from django.db import models as m

from app_sale.models.base import BaseEntity
from app_sale.models.product import Product


class Cart(BaseEntity):
    products = m.ManyToManyField(Product, null=True)
    total = m.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = m.BooleanField(default=True)

    def __str__(self):
        return self.total
