from django import forms as f
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea

from app_sale.models.product import Product


class ProductForm(f.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter Product Name'}),
            'product_category': Select(attrs={'class': 'form-control', 'id': 'product_category'}),
            'price': NumberInput(attrs={'class': 'form-control', 'id': 'price'}),
            'description': Textarea(attrs={'class': 'form-control', 'id': 'description'}),
            'product_image': FileInput(attrs={'class': 'form-control', 'id': 'product_image'})
        }
