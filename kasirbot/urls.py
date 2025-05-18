from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Root URL: form login
    path(
        '',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),

    # Logout: redirect kembali ke '/'
    path(
        'logout/',
        LogoutView.as_view(next_page='/'),
        name='logout'
    ),

    # Semua fitur inventory di bawah /dashboard/
    path('dashboard/', include('inventory.urls')),
]
