from django.contrib import admin
from .models import Product, StockLog, WebhookSetting

admin.site.register(Product)
admin.site.register(StockLog)
admin.site.register(WebhookSetting)
