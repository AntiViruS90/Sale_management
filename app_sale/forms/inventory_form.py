from django import forms as f
from django.forms import TextInput, Select, NumberInput, Textarea

from app_sale.models.inventory import Inventory


class InventoryForm(f.ModelForm):
    picture = f.ImageField(widget=f.ClearableFileInput(attrs={'class': 'form-control', 'id': 'picture'}))

    class Meta:
        model = Inventory
        fields = '__all__'
        widget = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Inventory Name'}),
            'category_name': Select(attrs={'class': 'form-control', 'id': 'category_name'}),
            'tags': Select(attrs={'class': 'form-control', 'id': 'tags', 'multiple': 'none'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'id': 'short_description',
                                                  'placeholder': "Enter inventory's short description"}),
            'full_description': Textarea(attrs={'class': 'form-control', 'id': 'full_description', 'rows': 5,
                                                'placeholder': "Enter inventory's full description'"}),
            'current_stock': NumberInput(attrs={'class': 'form-control', 'id': 'current_stock'}),
            'purchase_price': NumberInput(attrs={'class': 'form-control', 'id': 'purchase_price'}),
            'sales_price': NumberInput(attrs={'class': 'form-control', 'id': 'sales_price'}),
            'promotional_price': NumberInput(attrs={'class': 'form-control', 'id': 'promotional_price'}),
            'picture': f.ClearableFileInput(attrs={'class': 'form-control', 'id': 'picture'}),
        }
