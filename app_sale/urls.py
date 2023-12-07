from django.urls import path
from app_sale.views.dashboard_view import Dashboard
from app_sale.views.auth_view import UserLoginView, LogoutView
from app_sale.views.category_view import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView
from app_sale.views.inventory_view import InventoryCreateView, InventoryListView, InventoryDetailView, \
    InventoryUpdateView, InventoryDeleteView
from app_sale.views.tag_view import CreateListTagView, TagDeleteView, TagListView
from app_sale.views.product_view import CreateProductView, ProductListView

from app_sale.views.pos_view import POSView, cart_add, cart_updated, cart_remove
from app_sale.views.order_views import bulling_information_view, OrderItemView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('create-inventory/', InventoryCreateView.as_view(), name='create_inventory'),
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<pk>', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory-update/<pk>', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory-delete/<pk>', InventoryDeleteView.as_view(), name='inventory_delete'),
    path('tag-create/', CreateListTagView.as_view(), name='create_list_tag'),
    path('tag/', TagListView.as_view(), name='tag_list'),
    path('tag/<pk>', TagDeleteView.as_view(), name='tag_delete'),
    path('create-product/', CreateProductView.as_view(), name='product_create'),
    path('product-list/', ProductListView.as_view(), name='product_list'),
    path('cart/<int:id>/', cart_add, name='cart_add'),
    path('cart-update/<int:id>/', cart_updated, name='cart_updated'),
    path('cart-remove/<int:id>/', cart_remove, name='cart_remove'),
    path('pos/', POSView.as_view(), name='pos_view'),
    path('bulling-information/', bulling_information_view, name='bulling_information'),
    path('order-information/', OrderItemView.as_view(), name='order_information'),

]