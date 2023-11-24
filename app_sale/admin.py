from django.contrib import admin

from app_sale.models.category import Category
from app_sale.models.tag import Tag
from app_sale.models.inventory import Inventory
from app_sale.models.product import Product
from app_sale.models.order import Order, OrderItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'created_at', 'update_at']
    list_display_links = ['name', 'parent']
    list_filter = ['name']
    list_per_page = 8


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_name', 'current_stock', 'purchase_price',
                    'sales_price', 'promotional_price']
    list_display_links = ['name', 'category_name']
    list_editable = ['current_stock', 'purchase_price', 'sales_price', 'promotional_price']
    list_filter = ['name', 'current_stock']
    search_fields = ['name', 'purchase_price', 'sales_price', 'promotional_price']
    list_per_page = 8


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)