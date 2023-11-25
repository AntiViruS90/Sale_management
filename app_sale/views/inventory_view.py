from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from app_sale.models.inventory import Inventory
from app_sale.forms.inventory_form import InventoryForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateInventoryView(SuccessMessageMixin, CreateView):
    template_name = 'inventory/create_inventory.html'
    model = Inventory
    form_class = InventoryForm
    success_message = "Inventory created successfully!"
    success_url = '/create-inventory/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class InventoryListView(ListView):
    template_name = 'inventory/inventory_list.html'
    model = Inventory
    context_object_name = 'inventory'
    paginate_by = 10


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class InventoryDetailView(DetailView):
    template_name = 'inventory/inventory_details.html'
    model = Inventory
    context_object_name = 'inventory'


class InventoryUpdateView(UpdateView):
    template_name = 'inventory/create_inventory.html'
    model = Inventory
    form_class = InventoryForm
    success_url = '/inventory/'


@method_decorator(login_required(login_url = '/login/'), name = 'dispatch')
class InventoryDeleteView(DeleteView):
    template_name = 'inventory/inventory_confirm_delete.html'
    model = Inventory