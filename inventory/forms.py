from django import forms

class ExcelUploadForm(forms.Form):
    file = forms.FileField()

class MinStockForm(forms.Form):
    min_stock = forms.IntegerField(min_value=0)

class WebhookForm(forms.Form):
    url = forms.URLField()
