from django.db import models as m
from django.urls import reverse

from app_sale.models.base import BaseEntity
from app_sale.models.category import Category
from app_sale.models.tag import Tag


class Inventory(BaseEntity):
    name = m.CharField(max_length=120)
    category_name = m.ForeignKey(Category, on_delete=m.CASCADE, related_name='productCategory')
    short_description = m.CharField(max_length=250)
    full_description = m.TextField()
    current_stock = m.IntegerField(default=0)
    purchase_price = m.IntegerField(default=0)
    sales_price = m.IntegerField(default=0)
    promotional_price = m.IntegerField(default=0)
    tags = m.ManyToManyField(Tag, blank=True, related_name='inventory_tag')
    picture = m.ImageField(upload_to='inventory', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory_list', args=[self.id])
