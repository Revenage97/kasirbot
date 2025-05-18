from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root → login page
    path(
        '',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    # Logout (via POST oleh form di base.html atau link)
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Semua halaman dashboard Anda di-prefix /dashboard/
    path('dashboard/', include('inventory.urls')),
]
