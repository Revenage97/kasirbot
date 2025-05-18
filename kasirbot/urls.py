from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    # ← tambahkan baris ini untuk login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]
