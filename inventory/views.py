from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.http import JsonResponse
from .models import Product, StockLog, WebhookSetting
from .forms import ExcelUploadForm, MinStockForm, WebhookForm
import openpyxl, requests

def dashboard(request):
    pass

def upload_excel(request):
    pass

def webhook_settings(request):
    pass

def view_logs(request):
    pass

def send_to_telegram(request, product_id):
    pass
