from django.db import models as m

from app_sale.models.base import BaseEntity
from app_sale.models.category import Category


class Product(BaseEntity):
    title = m.CharField(max_length=200)
    description = m.TextField()
    product_category = m.ForeignKey(Category, on_delete=m.CASCADE, related_name='product')
    price = m.IntegerField(default=0)
    product_image = m.ImageField(upload_to='product')

    def __str__(self):
        return self.title
