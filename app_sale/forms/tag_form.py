from django import forms as f
from django.forms import TextInput

from app_sale.models.tag import Tag


class TagForm(f.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
        widget = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        }

