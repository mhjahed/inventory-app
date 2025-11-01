# store/admin.py

from django.contrib import admin
from .models import Product, Customer, Sale, SaleItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'quantity', 'selling_price', 'is_low_stock']
    list_filter = ['category']
    search_fields = ['name', 'sku']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone']

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['invoice_no', 'date', 'cashier', 'customer', 'total_amount', 'payment_method']
    list_filter = ['date', 'payment_method', 'cashier']
    search_fields = ['invoice_no', 'customer__name']
    inlines = [SaleItemInline]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['sale', 'product', 'quantity_sold', 'unit_price', 'subtotal']