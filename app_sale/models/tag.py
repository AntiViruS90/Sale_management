from django.db import models as m

from app_sale.models.base import BaseEntity


class Tag(BaseEntity):
    name = m.CharField(max_length=80)

    def __str__(self):
        return self.name
