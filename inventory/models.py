from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=0)
    min_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class StockLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product.name} - {self.action}"

class WebhookSetting(models.Model):
    url = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)
