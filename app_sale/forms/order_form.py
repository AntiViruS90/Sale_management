from django.forms import ModelForm, TextInput, NumberInput, EmailInput

from app_sale.models.order import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'full_name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Your Full Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Your Email Address'}),
            'phn_number': NumberInput(attrs={'class': 'form-control', 'id': 'phn_number'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Your Address'})
        }
