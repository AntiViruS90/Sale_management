from django import forms as f
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea

from app_sale.models.product import Product


class ProductForm(f.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'id': 'title', 'placeholder': 'Enter Product Name'}),
            'product_category': Select(attrs={'id': 'product_category'}),
            'price': NumberInput(attrs={'id': 'price'}),
            'description': Textarea(attrs={'id': 'description'}),
            'product_image': FileInput(attrs={'class': 'form-control', 'id': 'product_image'})
        }
