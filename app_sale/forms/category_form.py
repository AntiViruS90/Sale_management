from django import forms as f
from django.forms import TextInput, Select, FileInput, CheckboxInput

from app_sale.models.category import Category


class CategoryForm(f.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'parent': Select(attrs={'class': 'form-control'}),
            'category_image': FileInput(attrs={'class': 'form-control', 'id': 'imageUpload'}),
            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'})
        }
