from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Auth
    path('login/', views.cashier_login, name='login'),
    path('logout/', views.cashier_logout, name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('search/products/', views.search_products, name='search_products'),

    # Billing
    path('billing/', views.billing, name='billing'),
    path('invoice/<int:sale_id>/print/', views.print_invoice, name='print_invoice'),

    # Customers
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/<int:pk>/history/', views.customer_history, name='customer_history'),

    # Reports
    path('reports/', views.reports, name='reports'),
    path('reports/export/', views.export_sales_report, name='export_sales_report'),
    path('accounts/login/', views.cashier_login, name='account_login'),
    path('logout/', views.cashier_logout, name='logout'),
]