from django.db import models as m
from django.contrib.auth.models import User

from app_sale.models.base import BaseEntity


class Customer(BaseEntity):
    owner = m.OneToOneField(User, related_name='customers', on_delete=m.SET_DEFAULT)
    phone_number = m.CharField(max_length=20, unique=True)
    shop_name = m.CharField(max_length=100, unique=True)
    nid_number = m.IntegerField(max_length=20, unique=True)
    trea_liance = m.CharField(max_length=60, unique=True)
    address = m.TextField(blank=True)
    profile_picture = m.ImageField(upload_to='customer/%Y/%m/%d', null=True, blank=True)
    is_active = m.BooleanField(default=True)

    def __str__(self):
        return self.shop_name[:15]
