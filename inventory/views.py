from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.http import JsonResponse
from .models import Product, StockLog, WebhookSetting
from .forms import ExcelUploadForm, MinStockForm, WebhookForm
import openpyxl, requests

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html', {
        'products': products
    })

def upload_excel(request):
    form = ExcelUploadForm()
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            sheet = wb.active
            for row in sheet.iter_rows(min_row=2, values_only=True):
                name, stock = row[0], row[1]
                if name:
                    product, created = Product.objects.get_or_create(name=name)
                    product.stock = stock
                    product.save()
                    StockLog.objects.create(product=product, action="upload_excel")
            return redirect('dashboard')
    return render(request, 'inventory/upload.html', {'form': form})

def webhook_settings(request):
    webhook = WebhookSetting.objects.first()
    if request.method == 'POST':
        form = WebhookForm(request.POST)
        if form.is_valid():
            if webhook:
                webhook.url = form.cleaned_data['url']
                webhook.save()
            else:
                WebhookSetting.objects.create(url=form.cleaned_data['url'])
            return redirect('webhook_settings')
    else:
        form = WebhookForm(initial={'url': webhook.url if webhook else ''})
    return render(request, 'inventory/settings.html', {'form': form})

def view_logs(request):
    seven_days_ago = timezone.now() - timezone.timedelta(days=7)
    logs = StockLog.objects.filter(timestamp__gte=seven_days_ago).order_by('-timestamp')
    return render(request, 'inventory/logs.html', {'logs': logs})

def send_to_telegram(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    webhook = WebhookSetting.objects.first()
    if webhook:
        payload = {
            'product': product.name,
            'stock': product.stock,
            'min_stock': product.min_stock,
        }
        try:
            requests.post(webhook.url, json=payload)
            StockLog.objects.create(product=product, action="send_to_telegram")
        except Exception as e:
            print("Gagal kirim:", e)
    return redirect('dashboard')
