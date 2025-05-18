# inventory/urls.py
from django.urls import path
from . import views

app_name = 'inventory'  # opsional, untuk namespacing URL

urlpatterns = [
    # Dashboard stok
    path('', views.dashboard, name='dashboard'),

    # Fitur upload Excel
    path('upload/', views.upload_excel, name='upload_excel'),

    # Pengaturan webhook
    path('settings/', views.webhook_settings, name='webhook_settings'),

    # Lihat logs
    path('logs/', views.view_logs, name='view_logs'),

    # Kirim satu produk ke Telegram
    path('send/<int:product_id>/', views.send_to_telegram, name='send_to_telegram'),
]
