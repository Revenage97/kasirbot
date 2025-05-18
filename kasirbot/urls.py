# kasirbot/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Halaman root menampilkan LoginView
    path(
        '',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),

    # Logout via POST (dengan form di base.html)
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # Setelah login, semua dashboard di bawah /dashboard/
    path(
        'dashboard/',
        include('inventory.urls')
    ),
]
