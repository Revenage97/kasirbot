from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('settings/', views.webhook_settings, name='webhook_settings'),
    path('logs/', views.view_logs, name='view_logs'),
    path('send/<int:product_id>/', views.send_to_telegram, name='send_to_telegram'),
]
