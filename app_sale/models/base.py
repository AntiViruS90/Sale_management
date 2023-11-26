from django.db import models as m


class BaseEntity(m.Model):
    created_at = m.DateTimeField(auto_now_add=True)
    update_at = m.DateTimeField(auto_now=True)