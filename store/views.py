# store/views.py — COMPLETE

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum, Count, Q
from django.utils import timezone
import json
from decimal import Decimal
import openpyxl
from datetime import date, timedelta
from .models import Product, Customer, Sale, SaleItem
from .forms import ProductForm

# === AUTH ===
def cashier_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff and not user.is_superuser:
            login(request, user)
            return redirect('store:dashboard')
        else:
            messages.error(request, "Invalid credentials or not authorized as cashier.")
    return render(request, 'login.html')

def cashier_logout(request):
    logout(request)
    return redirect('store:login')

# === DASHBOARD ===
@login_required
def dashboard(request):
    today = date.today()

    total_sales_today = Sale.objects.filter(date__date=today).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_customers_today = Sale.objects.filter(date__date=today).count()
    total_products_in_stock = Product.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0

    top_products = SaleItem.objects.filter(
        sale__date__gte=today - timedelta(days=30)
    ).values('product__name').annotate(
        total_sold=Sum('quantity_sold')
    ).order_by('-total_sold')[:5]

    low_stock_products = Product.objects.filter(quantity__lt=5)

    # Chart Data: Last 7 Days Sales
    dates = [(today - timedelta(days=i)) for i in range(6, -1, -1)]
    daily_sales = []
    for d in dates:
        total = Sale.objects.filter(date__date=d).aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        daily_sales.append(float(total))
    day_labels = [d.strftime('%a') for d in dates]

    context = {
        'total_sales_today': total_sales_today,
        'total_customers_today': total_customers_today,
        'total_products_in_stock': total_products_in_stock,
        'top_products': top_products,
        'low_stock_products': low_stock_products,
        'chart_labels': day_labels,
        'chart_data': daily_sales,
    }
    return render(request, 'dashboard.html', context)

# === PRODUCTS ===
@login_required
def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(sku__icontains=query) | 
            Q(category__icontains=query)
        )
    return render(request, 'products/list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('store:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add.html', {'form': form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('store:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit.html', {'form': form, 'product': product})

# === SEARCH API ===
@login_required
def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(sku__icontains=query)
    )[:10]
    results = [{'id': p.id, 'name': p.name, 'sku': p.sku, 'price': float(p.selling_price)} for p in products]
    return JsonResponse({'results': results})

# === CUSTOMERS ===
@login_required
def customer_list(request):
    query = request.GET.get('q')
    customers = Customer.objects.all()
    if query:
        customers = customers.filter(
            Q(name__icontains=query) | 
            Q(phone__icontains=query)
        )
    return render(request, 'customers/list.html', {'customers': customers})

@login_required
def add_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        Customer.objects.create(name=name, phone=phone, email=email, address=address)
        messages.success(request, "Customer added!")
        return redirect('store:customer_list')
    return render(request, 'customers/add.html')

@login_required
def customer_history(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    sales = Sale.objects.filter(customer=customer).order_by('-date')
    return render(request, 'customers/history.html', {'customer': customer, 'sales': sales})

# === BILLING ===
@login_required
def billing(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Get or create customer
        customer_data = data.get('customer')
        customer = None
        if customer_data.get('name'):
            customer, created = Customer.objects.get_or_create(
                phone=customer_data['phone'],
                defaults={
                    'name': customer_data['name'],
                    'email': customer_data.get('email', ''),
                    'address': customer_data.get('address', '')
                }
            )

        # Generate unique invoice no
        last_sale = Sale.objects.order_by('-id').first()
        invoice_no = f"INV-{(last_sale.id + 1) if last_sale else 1:04d}"

        # Create Sale
        sale = Sale.objects.create(
            invoice_no=invoice_no,
            cashier=request.user,
            customer=customer,
            total_amount=Decimal(data['total_amount']),
            payment_method=data['payment_method']
        )

        # Create SaleItems & Deduct Stock
        for item in data['items']:
            product = Product.objects.get(id=item['product_id'])
            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity_sold=item['quantity'],
                unit_price=Decimal(item['unit_price']),
                subtotal=Decimal(item['subtotal'])
            )
            product.quantity -= item['quantity']
            product.save()

        return JsonResponse({'success': True, 'sale_id': sale.id})

    customers = Customer.objects.all()[:10]
    products = Product.objects.filter(quantity__gt=0)
    return render(request, 'billing/billing.html', {'customers': customers, 'products': products})

@login_required
def print_invoice(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    return render(request, 'billing/invoice_print.html', {'sale': sale})

# === REPORTS ===
@login_required
def reports(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    sales = Sale.objects.all().order_by('-date')
    if start_date and end_date:
        sales = sales.filter(date__date__gte=start_date, date__date__lte=end_date)

    low_stock = Product.objects.filter(quantity__lt=5)
    out_of_stock = Product.objects.filter(quantity=0)

    context = {
        'sales': sales,
        'low_stock': low_stock,
        'out_of_stock': out_of_stock,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'reports/reports.html', context)

@login_required
def export_sales_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    sales = Sale.objects.all()
    if start_date and end_date:
        sales = sales.filter(date__date__gte=start_date, date__date__lte=end_date)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sales Report"

    headers = ['Invoice No', 'Date', 'Cashier', 'Customer', 'Total Amount', 'Payment Method']
    ws.append(headers)

    for sale in sales:
        ws.append([
            sale.invoice_no,
            sale.date.strftime('%Y-%m-%d %H:%M'),
            sale.cashier.username,
            sale.customer.name if sale.customer else "Walk-in",
            float(sale.total_amount),
            sale.get_payment_method_display(),
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=sales_report.xlsx'
    wb.save(response)
    return response