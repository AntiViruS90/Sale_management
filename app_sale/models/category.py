from django.db import models as m
from django.urls import reverse

from app_sale.models.base import BaseEntity


class Category(BaseEntity):
    name = m.CharField(max_length=100, unique=True)
    parent = m.ForeignKey('self', on_delete=m.CASCADE, blank=True, null=True, related_name='sub_category')
    category_image = m.ImageField(upload_to='category/%Y/%m/%d', null=True, blank=True)
    is_active = m.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return Category.objects.filter(parent=self)

    def get_absolute_url(self):
        return reverse('category_list', args=[self.id])