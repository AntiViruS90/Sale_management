from django.shortcuts import render, redirect
from django.views.generic import ListView

from app_sale.models.order import OrderItem
from app_sale.forms.order_form import OrderForm
from app_sale.addcart import Cart


def bulling_information_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    orderItem=order,
                    products=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
        return redirect('pos_view')
    else:
        form = OrderForm()
    return render(request, 'pos/bulling_information.html', {'form': form, 'cart': cart})


class OrderItemView(ListView):
    template_name = 'pos/order_list.html'
    model = OrderItem
    context_object_name = 'order'
    paginate_by = 15