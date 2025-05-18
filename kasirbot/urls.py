from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '', 
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(next_page='/'),
        name='logout'
    ),
    path('dashboard/', include('inventory.urls')),
]
